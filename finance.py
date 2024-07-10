import requests

url = "https://fresh-linkedin-profile-data.p.rapidapi.com/search-jobs"

payload = {
	"keywords": "marketing",
	"geo_code": 92000000,
	"date_posted": "Any time",
	"experience_levels": [],
	"company_ids": [1035],
	"title_ids": [],
	"onsite_remotes": [],
	"functions": [],
	"industries": [],
	"job_types": [],
	"sort_by": "Most relevant",
	"easy_apply": "false",
	"under_10_applicants": "false",
	"start": 0
}
headers = {
	"x-rapidapi-key": "203df5b23bmsh89a0940a229aa49p19a84ajsne6f6b0209f56",
	"x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())