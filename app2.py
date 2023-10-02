import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
candidates_folder = "candidates"
candidate_descriptions = {}
all_selected_candidates = []

with open("job_description.txt", "r") as file:
            job_description = file.read()

# Przejdź przez pliki w folderze "candidates"
for filename in os.listdir(candidates_folder):
    if filename.endswith(".txt"):
        # Utwórz pełną ścieżkę do pliku
        file_path = os.path.join(candidates_folder, filename)

        # Otwórz plik i odczytaj jego zawartość jako opis kandydata
        with open(file_path, "r") as file:
            candidate_description = file.read()

        # Twórz prompt dla pojedynczego kandydata
        prompt = f"""
        Please select the top candidate for the job based on their description and provide a one-line justification.
        
        Candidate Description:
        {candidate_description}
        
        Job requirements description: {job_description}
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": prompt
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Wybór najlepszego kandydata z odpowiedzi OpenAI
        selected_candidate = response['choices'][0]['message']['content']
        
        # Dodaj wybranego kandydata do listy
        all_selected_candidates.append(selected_candidate)

# Wyświetl wyniki
for i, selected_candidate in enumerate(all_selected_candidates, start=1):
    print(f"Top Candidate {i}:\n{selected_candidate}\n")