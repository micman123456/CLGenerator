

ID = 0
SITE = 1
URL = 2
TITLE = 4
COMPANY = 5
LOCATION = 6
DATE = 8
SALARY_TYPE = 10
SALARY_RANGE_L = 11
SALARY_RANGE_U = 12
CURRENCY = 12
DESC = 20




def Construct_llama_Prompt(user_details, job):
    
    prompt = f"Can you create a professional, ready-to-send cover letter using the following details? Make sure to highlight relevant skills, experiences, and qualifications that match the job description.\n\n" \
             f"**About Me:**\n" \
             f"Full Name: {user_details['name']}\n" \
             f"Location: {user_details['location']}\n" \
             f"Email: {user_details['email']}\n" \
             f"Phone number: {user_details['number']}\n" \
             f"Experience: Previos jobs include {', '.join(user_details['experience'])}\n" \
             f"Education: I have a {user_details['education']} from {user_details['school']} studying {user_details['field']}\n" \
             f"Certifications: {', '.join(user_details['certs'])}\n" \
             f"Skills: {', '.join(user_details['skills'])}\n" \
             f"Programming Languages: {', '.join(user_details['languages'])}\n\n" \
             f"**About the Job:**\n" \
             f"Job Title: {job.iloc[TITLE]}\n" \
             f"Company: {job.iloc[COMPANY]}\n" \
             f"Location: {job.iloc[LOCATION]}\n" \
             f"Job Description: {job.iloc[DESC]}\n\n" \
             f"Please use this information to craft a compelling cover letter that showcases how my background in {user_details['field']} and my experience with {', '.join(user_details['skills'][:3])} " \
             f"make me a strong candidate for this position. Be sure to express enthusiasm for the role and the company."

    return prompt



def sendAIRequest(prompt):
    import ollama
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    print(response["message"]["content"])
    return response["message"]["content"]
