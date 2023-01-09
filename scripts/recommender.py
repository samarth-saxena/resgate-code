from utils import *

def read_resume(pdf_url):
    mapping_obj = Mapping()
    pdf_parser = ParsePDF(pdf_url)
    user_obj = JSON_extract(mapping_obj, pdf_parser)
    return user_obj.json()

def top_picks(pdf_url,projects):
    recommender = Recommender()
    user_profile = read_resume(pdf_url)
    recommendations = recommender.generate_recommendations(user_profile,projects)
    
    return recommendations[:5] 