from typing import List
from fastapi import FastAPI, HTTPException
from . import data
from . import schema

app = FastAPI(
    title="Cluster API", description="Malaysia cluster API service", version="1.0"
)


@app.get("/cluster/statistic", response_model=schema.StatisticModel)
def get_cluster_statistic():
    return data.cluster_statistic()


@app.get("/cluster/latest", response_model=List[schema.ClusterBase])
def get_cluster_latest():
    latest_cluster = data.cluster_latest()
    if latest_cluster is None:
        HTTPException(status_code=404, detail="No latest cluster")
    return latest_cluster


@app.get("/cluster/category/{category_name}", response_model=List[schema.ClusterBase])
def get_cluster_by_category(category_name: str):
    cluster_cat = data.cluster_category(category_name)
    if cluster_cat == []:
        raise HTTPException(
            status_code=404,
            detail="Cluster category not exist.",
        )
    return cluster_cat


@app.get("/cluster/state/{state_name}", response_model=List[schema.ClusterBase])
def get_cluster_by_state(state_name: str):
    cluster = data.cluster_state(state_name)
    if cluster is None:
        raise HTTPException(status_code=404, detail="State Not found")

    return cluster


@app.get("/cluster/{id}", response_model=schema.ClusterBase)
def get_cluster_by_id(id: int):
    single_cluster = data.cluster(id)
    if single_cluster is None:
        raise HTTPException(status_code=404, detail="Data Not found")

    return single_cluster


@app.post("/cluster/search", response_model=List[schema.ClusterBase])
def search_cluster(search: schema.SearchQuery):
    list_cluster = data.cluster_list(search=search)
    if list_cluster is None:
        raise HTTPException(status_code=404, detail="Data Not found")

    return list_cluster
