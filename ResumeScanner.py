# Import Libraries
# using TF-IDF, which is term frequency, inverse document frequency, to identify keywords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer # This converts text into numerical features by calculating TF-IDF scores, allowing us to extract keywords.
from sklearn.metrics.pairwise import cosine_similarity

# Sample resumes and job description data
data = {
    'resume_id' : [1,2,3],
    'resume_text' : [
        "Experienced data scientist with skills in Python, machine learing and data analysis.",
        "Software developer with expertise in Java, cloud computing and project management",
        "Data analyst with proficiency in SQL, Python, and data visulaization."
    ],
}

job_description = "Looking for a data scientist skilled in Python, machine learning, SQL, and data analysis."

# Covert to dataframe
df = pd.DataFrame(data)
print("Resumes : \n",df)

# Combine job description with resumes for TF-IDF vectorization
documents = df['resume_text'].tolist()
documents.append(job_description)

# Initialize the TfidVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tdidf_matrix = vectorizer.fit_transform(documents)

# Calculate the similarity scores between job description and each resume
similarity_score = cosine_similarity(tdidf_matrix[-1], tdidf_matrix[:-1]).flatten()

# Display the similarity scores for each resume
df['similarity_score'] = similarity_score
print("\nResume Similarity Scores:\n",df[['resume_id', 'similarity_score']])

# Identify resumes that match job requirements (threshold can be adjusted)
threshold = 0.2
matching_resumes = df[df['similarity_score'] >= threshold]
print("\nResume matching the job requirements:\n", matching_resumes[['resume_id','similarity_score']])




