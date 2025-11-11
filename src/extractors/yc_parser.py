thonimport json

def parse_company_info(company_data):
    """Parses individual company data."""
    company_info = {
        'company_name': company_data['company_name'],
        'batch': company_data['batch'],
        'status': company_data['status'],
        'location': company_data['location'],
        'year_founded': company_data['year_founded'],
        'website': company_data['website'],
        'founders': company_data['founders'],
    }
    return company_info

def parse_job_info(company_data):
    """Parses open job postings."""
    jobs = []
    for job in company_data.get('open_jobs', []):
        job_info = {
            'title': job['title'],
            'location': job['location'],
            'salary': job['salary'],
            'years_experience': job['years_experience'],
            'description': job['description'],
        }
        jobs.append(job_info)
    return jobs