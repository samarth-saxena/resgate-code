from .utils import *
import os

def read_resume(pdf_url):
    mapping_obj = Mapping()
    pdf_parser = ParsePDF(pdf_url)
    user_obj = JSON_extract(mapping_obj, pdf_parser)
    return user_obj.json()

def top_picks(pdf_url,projects):
    recommender = Recommender()
    user_profile = read_resume("C:/Mihir/IIITD/Anveshan/ResGate_v2/resgate-code/media/resumes/Resume_IIITD_placement.pdf")
    print("Student Features")
    print(user_profile)
    recommendations = recommender.generate_recommendations(user_profile,projects)
    i = 1
    for rec in recommendations:
        print(f"{i}. {rec[0]['title']} with {100*(1-rec[1])}% match")
    return recommendations 