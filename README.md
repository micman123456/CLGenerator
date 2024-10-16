# Job Scraper and Cover Letter Generator

This project is a **Job Scraper and Cover Letter Generator** powered by Jobspy and Llama 3. It allows you to scrape multiple job boards, including Indeed, Glassdoor, ZipRecruiter, and LinkedIn, to find relevant job postings. Additionally, it offers an option to generate a professional cover letter for any job found, saving it to a `.docx` file.

## Features

- Scrapes job listings from **Indeed**, **Glassdoor**, **ZipRecruiter**, and **LinkedIn**.
- Provides a search interface where users can specify job title/keywords, location, and more.
- Option to include **remote jobs** in the search.
- **Generates a tailored cover letter** for the job listings found, using AI powered by **Llama 3**.
- Saves generated cover letters in `.docx` format for easy sharing.

## Powered By

- **Job Scraper**: [JobSpy](https://github.com/Bunsly/JobSpy)
- **Cover Letter Generator**: AI model **Llama 3**

## Requirements

- **Python** 3.10
- **Ollama**: Used for generating cover letters. [Installation Instructions](https://ollama.com/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/CLGenerator.git
    cd CLGenerator
    ```

2. Set up a virtual environment and install the required packages:

    ```bash
    python3.10 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Install **ollama** following the instructions [here](https://ollama.com/).

## Usage

1. Run the script:

    ```bash
    python DisplayJobs.py
    ```

2. Enter your search parameters (job title, location, etc.) when prompted.

3. The program will scrape jobs from the selected sites and display the results.

4. Choose a job from the list to generate a cover letter, which will be saved to a `.docx` file.

## Example Flow

1. **Enter Job Details**: Specify the job title/keyword, country, province/state, city, and sites you want to scrape from.

2. **Search**: The script scrapes job boards for relevant listings.

3. **Generate Cover Letter**: For each job found, choose an option to generate a cover letter tailored to the job description using AI.

4. **Save**: The generated cover letter is saved in a `.docx` format.

## Contributing

Feel free to open issues or contribute by submitting pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- **JobSpy** for scraping job listings: [JobSpy GitHub Repository](https://github.com/Bunsly/JobSpy)
- **Llama 3** for powering AI-generated cover letters.
