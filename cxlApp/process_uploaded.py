import pandas as pd
import os

def process_uploaded_files(uploaded_files):
    responses = []

    for uploaded_file in uploaded_files:
        try:
            # Use pandas to read the uploaded Excel file
            df = pd.read_excel(uploaded_file)

            # Extract the header (first row)
            header = df.columns.tolist()

            # Create a new DataFrame with only the header
            new_df = pd.DataFrame(columns=header)

            # Specify the path to save the generated Excel file
            save_path = r'C:\Users\raja0\OneDrive\Desktop\uploaded Excel extract its header'

            # Ensure the directory exists
            os.makedirs(save_path, exist_ok=True)

            # Generate the file name dynamically or use a fixed name
            file_name = 'header_only.xlsx'

            # Save the DataFrame to Excel format
            full_path = os.path.join(save_path, file_name)
            new_df.to_excel(full_path, index=False)

            # Optionally, you can return a response with the saved file path
            responses.append({"message": "File saved successfully", "file_path": full_path})

        except Exception as e:
            responses.append({"error": str(e)})

    return responses
