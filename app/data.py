from unicodedata import category

from .malaysia.state import states_list
import pandas as pd
from . import schema


# Prepare data in pandas / Load Data
cluster_data = pd.read_csv(
    "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/clusters.csv"
)
data = pd.DataFrame(cluster_data)
cluster_api = data.reset_index(inplace=True)
cluster_api = data.rename(columns={"index": "cluster_id"})


# Get last update from MOH
def last_update():
    return cluster_api.iloc[-1:]["date_announced"].item()


# Endpoint: /cluster/state/{state_name}
# {state, state_code, total_cluster, active_cluster}, {last_update}
def cluster_state(state_name: str):
    for state in states_list():

        if state_name.capitalize() == state:
            state_code = states_list()[state]

            try:
                return cluster_api.loc[
                    cluster_api["state"]
                    .astype(str)
                    .str.contains(r"\b{}\b".format(state_code))
                ].to_dict("records")

            except IndexError as e:
                return e


# Endpoint: /cluster/latest/ "No parameter & Query"
# Return array {state, state_code, cluster_name, date_announce, cluster_category, new_cases, total_cases}, {total_cluster}, {last_update}
# return high cases first
def cluster_latest():
    last_announced = last_update()
    try:
        return (
            cluster_api.query(
                f"date_announced == '{last_announced}' and status == 'active'"
            )
            .sort_values("cases_total", ascending=False)
            .to_dict("records")
        )
    except IndexError as e:
        return e


# Endpoint: /cluster/category/{category_name} "Short by active"
# {category, date_announce, cluster_name, state, district, status}, {last_update}
def cluster_category(cat_name: str):

    try:

        return cluster_api.loc[cluster_api["category"].isin([cat_name])].to_dict(
            "records"
        )
    except IndexError as e:
        return e


# Endpoint: /cluster/list "Query request" {date_announce, state_name, state_code, status} OR all list {Asscendig}
# {all_data}
def cluster_list(search: schema.SearchQuery):

    try:

        return cluster_api.loc[
            cluster_api["cluster"].str.contains(search.search_cluster, case=False)
        ].to_dict("records")

    except IndexError as e:
        return e


# Endpoint: /cluster/{index_id}
# {all_data}
def cluster(id: int):
    # add state name instead code state
    return cluster_api.iloc[id].to_dict()


def count_cluster():
    #  cat_count_total = cluster_dataset['category'].value_counts().to_dict()
    # total_active = cluster_dataset[cluster_dataset['status'] == 'active'].index.size
    return cluster_api.index.size


def count_active_cluster():
    return cluster_api[cluster_api["status"] == "active"].index.size


def count_cat_cluster():
    return cluster_api["category"].value_counts().to_dict()


# Total cluster
# total active cluster
# total based on category
def cluster_statistic():
    return {
        "total_cluster": count_cluster(),
        "total_active": count_active_cluster(),
        "category": [
            {
                "cat_workplace": count_cat_cluster()["workplace"],
                "cat_education": count_cat_cluster()["education"],
                "cat_religious": count_cat_cluster()["religious"],
                "cat_community": count_cat_cluster()["community"],
                "cat_highRisk": count_cat_cluster()["highRisk"],
                "cat_detentionCentre": count_cat_cluster()["detentionCentre"],
                "cat_import": count_cat_cluster()["import"],
            }
        ],
    }
