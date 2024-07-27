import argparse
import logging
from pypdf import PdfReader, PdfWriter

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def split_pdf(input_file: str):
    try:
        reader = PdfReader(input_file)
        menu_option: str = 'c'
        while menu_option != 'q':
            page_range = input(
                'Please put page(s) to be splitted: '
            ).strip()
            if not page_range:
                raise ValueError(f'Invalid page range: {page_range}')
            output_file = input('Enter the output pdf file name: ').strip() or "output.pdf"
            output_pdf = PdfWriter()
            page_ranges = page_range.split(',') or []
            for page_range in page_ranges:
                page_range_info = page_range.strip().split('-')
                start_page = int(page_range_info[0])
                end_page = int(page_range_info[-1])
                for i in range(start_page, end_page+1):
                    output_pdf.add_page(reader.pages[i-1])
                logger.info(f"Added {start_page} to {end_page} to output file")
            output_pdf.write(output_file)
            logger.info(f"Finish writing to {output_file}")
            # Continue or exit
            menu_option = str(input("Press Q to exit: ").strip() or "c").lower()
        logger.info("Finish splitting the file.")
    except Exception as e:
        logger.error(f"Failed to split PDF: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PDF Utility')
    parser.add_argument('command')
    parser.add_argument('--input-file', type=str, required=True)
    args = parser.parse_args()
    command = args.command.lower()

    if command == 'split':
        split_pdf(input_file=args.input_file)

