## Malaysia COVID-19 Cluster API
For education purpose only. Data can be found here:  https://github.com/MoH-Malaysia/covid19-public

## API Endpoint
- `cluster/state/{state_name}` 
    - Get list of cluster based on state name. 
        - `Johor`
        - `Kedah`
        - `Kelantan`
        - `Melaka`
        - `Negeri Sembilan`
        - `Pahang`
        - `Pulau Pinang`
        - `Perak`
        - `Perlis`
        - `Selangor`
        - `Terengganu`
        - `Sabah`
        - `Sarawak`
        - `KL`
        - `Labuan`
        - `Putrajaya`
        - `N/A`
- `cluster/latest`
    - List latest cluster
    - Example output:
    ```
    [
        {
            "cluster_id": 6682,
            "cluster": "KLUSTER KUNDUR HILIR",
            "state": "5",
            "district": "REMBAU, SEREMBAN",
            "date_announced": "2022-02-18",
            "date_last_onset": "2022-02-17",
            "category": "education",
            "status": "active",
            "cases_new": 42,
            "cases_total": 68,
            "cases_active": 68,
            "tests": 377,
            "icu": 0,
            "deaths": 0,
            "recovered": 0,
            "summary_bm": "Kluster ini dikenalpasti hasil saringan bersasar melibatkan pelajar-pelajar sebuah institusi pendidikan yang terletak di Kampung Kundur Hilir, Pedas, Rembau.",
            "summary_en": "This cluster was identified as a result of targeted screening involving students of an educational institution located at Kampung Kundur Hilir, Pedas, Rembau."
        },
        ...
        ...
    ]
    ```
- `cluster/category/{category_name}`
    - List cluster based on category name
        - `workplace`
        - `education`
        - `religious`
        - `community`
        - `highRisk`
        - `detentionCentre`
        - `import`
- `cluster/search`
    - Search cluster name
- `cluster/{id}`
    - Display single cluster data, based on index `id`
    - Example output <br>

- `cluster/statistic`
    - Get statistic of cluster
    - Example output<br>
    ```
    {
        "total_cluster": 6692,
        "total_active": 486,
        "category": [
            {
                "cat_workplace": 3480,
                "cat_education": 735,
                "cat_religious": 180,
                "cat_community": 1728,
                "cat_highRisk": 371,
                "cat_detentionCentre": 145,
                "cat_import": 53
            }
        ]
        }
    ```

### API Documentation
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## How to setup
Require python version >=3.9

### 1. Create environment
`python3 -m venv venv`

### 2. Activate environment
`source venv/bin/activate` (Linux/MacOS)
`venv\scripts\activate` (Windows)

### 3. Install package
`pip install -r requirements.txt`

### 4. Run
`uvicorn app.main:app --reload`

