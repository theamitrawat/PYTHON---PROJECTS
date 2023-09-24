import PyPDF2
import os

class PdfMerger:
    def __init__(self, input_files, output_file):
        self.input_files = input_files
        self.output_file = output_file

    def merge_pdfs(self):
        # Create a PdfFileMerger object
        pdf_merger = PyPDF2.PdfMerger()

        try:
            # Loop through the input PDF files
            for pdf_file in self.input_files:
                # Append each PDF file to the merger
                pdf_merger.append(pdf_file)

            # Write the merged PDF to the output file
            with open(self.output_file, 'wb') as merged_pdf:
                pdf_merger.write(merged_pdf)

            # Print a success message
            print(f"Merged PDF saved as '{self.output_file}'")

        except Exception as e:
            # Print an error message if something goes wrong
            print(f"Error merging PDFs: {str(e)}")

if __name__ == "__main__":
    # Replace these with the paths to your PDF files
    files = os.listdir(os.getcwd())
    input_files = []
    for file in files:
        if file.endswith(".pdf"):
            input_files.append(file)

    output_file = "merged.pdf"  # Specify the name of the output merged PDF

    # Create an instance of PdfMerger and call the merge_pdfs method
    pdf_merger = PdfMerger(input_files, output_file)
    pdf_merger.merge_pdfs()
