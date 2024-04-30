######################################################
### Super Simple PDF Scraper #########################
### Written by Christopher Eide, Technology ##########
### Integration Specialist, Trumbull Public Schools ##
### Initial Code Deposit: 30 Apr, 2024 ###############
### Direct inquiries to ceide@trumbullps.org #########
######################################################

import os, glob
from PyPDF2 import PdfReader

current_dir = os.path.dirname(__file__)
input_dir = os.path.join(current_dir, 'input')
output_dir = os.path.join(current_dir, 'output')

def main():
    # ensure input and output directories exist
    # create them if needed
    check_dirs()

    print(input_dir)

    # get a list of the pdfs in the input directory
    pdflist = glob.glob(os.path.join(input_dir,'*.pdf'))

    print(pdflist)

    # iterate through pdfs one at a time
    for file in pdflist:
        inputpdf = PdfReader(open(file, 'rb'))

        # set up the ouput string
        outputstring = ''

        # get the text from each page and append to output string
        for page in inputpdf.pages:
            page_text = page.extract_text()
            page_text = page_text.replace('\n', ' ')
            print(page_text)
            outputstring = outputstring + page_text
            #outputstring = outputstring + os.linesep
        
        # write to new .txt file in output dir
        output_file_name = os.path.splitext(os.path.basename(file))[0] + '.txt'
        output_file_path = os.path.join(output_dir, output_file_name)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(outputstring)

def check_dirs():
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

if __name__ == "__main__":
    main()