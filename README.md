# Resume Scanner Using TF-IDF and Cosine Similarity

## 🔎 Project Overview
This project demonstrates a Resume Scanner that evaluates resumes based on a given job description. Using **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity**, the program ranks resumes by their relevance to the job requirements.

---

## 📊 Features
- **Keyword Extraction**: Converts resumes and job descriptions into numerical features using TF-IDF.
- **Similarity Scoring**: Calculates similarity scores between the job description and each resume.
- **Dynamic Thresholding**: Filters resumes based on a customizable similarity score threshold.

---

## 📄 Data Requirements
The input consists of:
1. **Resumes**: Text data containing details of candidates.
2. **Job Description**: A string describing the desired qualifications and skills.

Sample data structure:
```python
{
    'resume_id': [1, 2, 3],
    'resume_text': [
        "Experienced data scientist with skills in Python, machine learning, and data analysis.",
        "Software developer with expertise in Java, cloud computing, and project management.",
        "Data analyst with proficiency in SQL, Python, and data visualization."
    ]
}
```

---

## 🔧 How It Works
1. **Load Resumes and Job Description**: Import sample resumes and job descriptions into a DataFrame.
2. **TF-IDF Vectorization**: Transform the text into numerical features to capture term importance.
3. **Cosine Similarity**: Measure the similarity between the job description and each resume.
4. **Filter Resumes**: Use a threshold to identify resumes most relevant to the job.

---

## 🚀 Getting Started
### Prerequisites
- Python 3.7+
- Required libraries:
  ```bash
  pip install pandas scikit-learn
  ```

### Run the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/Tanish141/resume-scanner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd resume-scanner
   ```
3. Execute the script:
   ```bash
   python resume_scanner.py
   ```

---

## 🎯 Example Output
### Input Data:
- **Resumes**: Sample text resumes.
- **Job Description**: "Looking for a data scientist skilled in Python, machine learning, SQL, and data analysis."

### Output:
```plaintext
Resume Similarity Scores:
   resume_id  similarity_score
0          1          0.780058
1          2          0.129276
2          3          0.520315

Resumes matching the job requirements:
   resume_id  similarity_score
0          1          0.780058
2          3          0.520315
```

---

## 🌐 Key Technologies
- **Pandas**: Data manipulation and analysis.
- **TF-IDF**: Feature extraction to quantify textual importance.
- **Cosine Similarity**: Measures textual similarity between resumes and job descriptions.

---

## 📢 Feedback
We welcome contributions and suggestions! Feel free to open issues or submit pull requests.
