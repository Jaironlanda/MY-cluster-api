from pydantic import BaseModel
from typing import Dict, List, Optional


class ClusterBase(BaseModel):
    cluster_id: int
    cluster: str
    state: str
    district: str
    date_announced: str
    date_last_onset: str
    category: str
    status: str
    cases_new: int
    cases_total: int
    cases_active: int
    tests: int
    icu: int
    deaths: int
    recovered: int
    summary_bm: str
    summary_en: str


class SearchQuery(BaseModel):
    search_cluster: str


class Category(BaseModel):
    cat_workplace: int
    cat_education: int
    cat_religious: int
    cat_community: int
    cat_highRisk: int
    cat_detentionCentre: int
    cat_import: int


class StatisticModel(BaseModel):
    total_cluster: int
    total_active: int
    category: List[Category]
