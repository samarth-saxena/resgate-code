import numpy
import nltk

import scipy 
import pandas as pd
import numpy as np
import transformers 
import torch

from transformers import *
from transformers import pipeline

from scipy.optimize import linear_sum_assignment

from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


class Mapping:
    def __init__(self):
        self.domain_mapping_dict = {
            'Artificial Intelligence': ["ai", "artificial intelligence"],
            'Applied Mathematics': ['maths', 'mathematics', "applied mathematics"],
            'Bioinformatics': ['bioinformatics', 'biology', 'bio'],
            'Cognitive Neuroscience': ['cogsci', 'cognitive neuroscience', 'cogscience'],
            'Computer Vision': ['cv', 'computer vision'],
            'Computer Graphics': ['graphics', 'computer graphics', 'cg'],
            'Computer Security and Cryptography': ['computer security', 'computer security and cryptography', 'cryptography', 'security', 'ns'],
            'Computer Networks & Systems': ['networks', 'computer networks', 'cn' , 'computer networks and systems'],
            'Database and Information Systems': ['dbms', 'information systems', 'database', 'db'],
            'Distributed Computing': ['distributed computing', 'parallel processing', 'parallel computing'],
            'Genomics': ['genes', 'genomics', 'gene'],
            'Game Theory': ['gt', 'game theory'],
            'Human- Computer Interaction': ['hci', 'human computer interaction'],
            'Big Data Management': ['big data', 'bd management', 'big data management', 'bigdata', 'semantic web'],
            'Machine Learning / Deep Learning': ["ml", 'machine learning', 'dl', 'deep learning', 'transformer', 'neural networks'],
            'Machine Learning / Optimisation / Signal Processing': ['information theory', 'signals', 'signal processing', 'mlops', 'ml ops', 'model optimisation'],
            'Natural Language Processing': ["nlp", 'natural language processing', 'text processing', 'natural language'],
            'Quantum Technologies / Computing': ['quantum computing', 'quantum', 'theory of computation', 'automata'],
            'Software Engineering': ['software engineering', 'web development', 'mobile development'],
            'Science and Technology Studies': ['social study', 'science nad technology studies'],
            'Theoretical Computer Science': ['theoretical computer science'],
            'Very Large Scale Integration [VLSI]': ["VLSI", 'Very Large Scale Integration', 'fpga'],
            'Virtualization': ['virtualization', 'virtualisation', 'cloud computing', 'cloud'],
            'Wireless Communication': ['wireless communication', 'wireless networks', 'optical networks']

        }
        self.skills_mapping_dict = {
            'Python': ['python', 'cpython'],
            'Java': ['java', 'oop'],
            'C++': ['c++', 'competitive programming', 'gnu'],
            'C#': ['c#', 'game design'],
            'JavaScript': ['javascript', 'typescript'],
            'PHP': ['php'],
            'SQL': ['sql', 'database management'],
            'R': ['r'],
            'Julia': ['julia'],
            'Swift': ['swift', 'ios'],
            "Data Analysis and Visualisation": ['powerbi', 'power bi', 'matplotlib'],
            'Machine Learning and Artificial Intelligence': ['ml', 'machine learning', 'tensorflow', 'pytorch', 'sklearn'],
            'Cloud Computing': ['cloud', 'aws', 'azure'],
            "DevOps": ['devops', 'dev ops', 'docker', 'kubernetes'],
            'Mobile App Development': ['flutter', 'react native', 'android'],
            "Web App Development": ['javascript', 'node', 'js', 'php', 'django', 'sass', 'flask', 'react'],
            "Linux": ['linux', 'operating system'],
            'MATLAB': ['matlab', 'simulink'],
            'Circuit design and simulation': ['spice', 'ltspice', 'orcad', 'cadence'],
            'Embedded systems': ['embedded systems', 'fpga', 'vivado', 'hls', 'hardware programming'],
            'VLSI Design': ['vlsi', 'circuit', 'fabrication'],
            'Internet of Things (IoT)': ['networks', 'sensors', 'rasberrypi', 'arduino', 'hardware']
        }
        self.SKILLS_DB = []
        self.DOMAIN_DB = []
    def get_domain_from_key(self):
        ans = {}
        for domain in self.domain_mapping_dict.keys():
            for word in self.domain_mapping_dict[domain]:
                ans[word] = domain
        return ans

    def get_skill_from_key(self):
        ans = {}
        for skill in self.skills_mapping_dict:
            for word in self.skills_mapping_dict[skill]:
                ans[word] = skill
        return ans

    def init_skills(self):
        for skill in self.skills_mapping_dict.keys():
            for word in self.skills_mapping_dict[skill]:
                self.DOMAIN_DB.append(word)
        return self.DOMAIN_DB

    def init_domain(self):
        for domain in self.domain_mapping_dict.keys():
            for word in self.domain_mapping_dict[domain]:
                self.SKILLS_DB.append(word)
        return self.SKILLS_DB



class ParsePDF:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
    
    
    def extract_text_from_pdf(self):
        self.text = extract_text(self.pdf_path)
        return self.text

    
    def extract_skills(self, SKILLS_DB):
        
        stop_words = set(nltk.corpus.stopwords.words('english'))
        text = self.extract_text_from_pdf()
        word_tokens = nltk.tokenize.word_tokenize(text)
    
        # remove the stop words
        #print(word_tokens)
        filtered_tokens = [w for w in word_tokens if w not in stop_words]
    
        # remove the punctuation
        filtered_tokens = [w for w in word_tokens if w.isalpha()]
    
        # generate bigrams and trigrams (such as artificial intelligence)
        bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
    
        # we create a set to keep the results in.
        found_skills = set()
    
        # we search for each token in our skills database
        for token in filtered_tokens:
            if token.lower() in SKILLS_DB:
                #found_skills.add(token)
                found_skills.add(token.lower())
    
        # we search for each bigram and trigram in our skills database
        for ngram in bigrams_trigrams:
            if ngram.lower() in SKILLS_DB:
                #found_skills.add(ngram)
                found_skills.add(ngram.lower())
    
        return list(found_skills)

    
    def extract_domains(self, DOMAIN_DB):
        stop_words = set(nltk.corpus.stopwords.words('english'))
        text = self.extract_text_from_pdf()
        word_tokens = nltk.tokenize.word_tokenize(text)
    
        # remove the stop words
        #print(word_tokens)
        filtered_tokens = [w for w in word_tokens if w not in stop_words]
    
        # remove the punctuation
        filtered_tokens = [w for w in word_tokens if w.isalpha()]
    
        # generate bigrams and trigrams (such as artificial intelligence)
        bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
    
        # we create a set to keep the results in.
        found_domains = set()
    
        # we search for each token in our skills database
        for token in filtered_tokens:
            if token.lower() in DOMAIN_DB:
                #found_skills.add(token)
                found_domains.add(token.lower())
    
        # we search for each bigram and trigram in our skills database
        for ngram in bigrams_trigrams:
            if ngram.lower() in DOMAIN_DB:
                #found_skills.add(ngram)
                found_domains.add(ngram.lower())
    
        return list(found_domains)



class JSON_extract:
    def __init__(self, mapping_obj, pdf_parser):
        self.mapping_obj = mapping_obj
        self.pdf_parser = pdf_parser

    def get_skills(self):
        SKILLS_DB = self.mapping_obj.init_skills()
        
        skill_keys = self.pdf_parser.extract_skills(SKILLS_DB)
        skill_dict = self.mapping_obj.get_skill_from_key()
        ans = []
        for key in skill_keys:
            ans.append(skill_dict[key])
        #print(ans)
        return list(set(ans))

    def get_domains(self):
        DOMAIN_DB = self.mapping_obj.init_domain()
        domain_keys = self.pdf_parser.extract_skills(DOMAIN_DB)
        domain_dict = self.mapping_obj.get_domain_from_key()
        ans = []
        for key in domain_keys:
            ans.append(domain_dict[key])
        #print(ans)
        return list(set(ans))

    def json(self):
        ans = {}
        ans["skills"] = self.get_skills()
        ans["domains"] = self.get_domains()
        return ans


class Recommender:
    
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
        self.model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased') 

    
    def embed_text(self, text):
        input_ids = torch.tensor(self.tokenizer.encode(text)).unsqueeze(0)  # Batch size 1
        # print(input_ids)
        outputs = self.model(input_ids)
        last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple
        return last_hidden_states.mean(1)

    
    def get_similiarity(self,em1,em2):
        return scipy.spatial.distance.cosine(em1.detach().numpy(),em2.detach().numpy())

    
    def get_entity_embedding(self,entity):
        dom_list = entity['domains']
        sk_list = entity['skills']
        
        em_dom_dict = {}
        em_sk_dict = {}
        
        for domain in dom_list:
            em_dom_dict[domain] = self.embed_text(domain,self.model)
        for skill in sk_list:
            em_sk_dict[skill] = self.embed_text(skill,self.model)
        
        return em_dom_dict,em_sk_dict

    
    def get_matching(self,user_nodes,project_nodes):
    
        df = pd.DataFrame(index=user_nodes.keys(),columns=project_nodes.keys())
        user_fields = list(user_nodes.keys())
        project_fields = list(project_nodes.keys())
        
        for i,u in enumerate(user_nodes.keys()):
            for j,p in enumerate(project_nodes.keys()):
                df.loc[u,p] = self.get_similiarity(
                    user_nodes[u],
                    project_nodes[p]
                )
        # print(df)
        cost_matrix = df.to_numpy().astype(float)
        # print(cost_matrix.shape)
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        matching = []
        for r in list(row_ind):
            for c in list(col_ind):
                matching.append((user_fields[r],project_fields[c]))
        matching_cost = cost_matrix[row_ind,col_ind].sum()
        
        return matching, matching_cost
    
    
    def get_cost(self,user,project):
        user_dom_nodes, user_skill_nodes = self.get_entity_embedding(user)
        project_dom_nodes, project_skill_nodes = self.get_entity_embedding(project)
        
        domain_matching, domain_matching_cost = self.get_matching(user_dom_nodes,project_dom_nodes)
        # print("--------------------------------------------------------------------------------")
        skill_matching, skill_matching_cost = self.get_matching(user_skill_nodes,project_skill_nodes)
        # print("--------------------------------------------------------------------------------")
        
        print(f"Domain Matching with total cost = {domain_matching_cost}")
        print(f"Skill Matching with total cost = {skill_matching_cost}")
        
        return 2*domain_matching_cost + skill_matching_cost


    def generate_recommendations(self,user,projects):
        cost_dict = {}
        for project_dict in projects:
            print("==================================================================================")
            print(f"Matching with {project_dict['title']}...")
            cost = self.get_cost(user,project_dict)
            if cost not in cost_dict.keys():
                cost_dict[cost] = [project_dict,]
            else: cost_dict[cost].append(project_dict)
        
        sorted_costs = sorted(list(cost_dict.keys()))
        max_cost = sorted_costs[-1]
        min_cost = sorted_costs[0]
        
        sorted_recs = []
        for cost in sorted_costs:
            for project in cost_dict[cost]:
                sorted_recs.append((project,(cost-min_cost)/(max_cost-min_cost)))
                
        return sorted_recs