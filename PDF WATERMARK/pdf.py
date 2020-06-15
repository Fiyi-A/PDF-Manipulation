import PyPDF2
import sys

'''
File1 - Get the Input file from terminal 
File2 - Get the Watermark file from terminal
'''
pdf_file = sys.argv[1]
watermark_file = sys.argv[2]

'''define a watermark function that takes in a pdf file and a watermark file'''
def watermark_pdf(file1 = 'dummy.pdf',file2 = 'wtr.pdf'):
	'''read the pdf file you want to watermark'''
	with open(file1,'rb') as fl1:
		read_file1 = PyPDF2.PdfFileReader(fl1)

		'''read the watermark file that you want to add on the pdf file'''
		with open(file2,'rb') as fl2:
			read_file2 = PyPDF2.PdfFileReader(fl2)
			# get the page for the watermark file, should be only 1
			page_file2 = read_file2.getPage(0)

			'''write into a new pdf that stores the watermarked pages'''
			with open('watermarked.pdf', 'wb') as fl3:
				# create a writer object that lets you write object in memory
				writer = PyPDF2.PdfFileWriter()
				# loop through each pdf file page and merge the watermark page on it
				for i in range(read_file1.getNumPages()):
					page_file1 = read_file1.getPage(i)
					page_file1.mergePage(page_file2)
					# add the watermark of the merged page each time it loops
					writer.addPage(page_file1)
					# write into the watermarked pdf using the writer object
					writer.write(fl3)

'''call watermark function'''
watermark_pdf(pdf_file,watermark_file)