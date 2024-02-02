# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# import pdfkit, os

# @login_required(login_url='login')
# def rsrch_generate_pdf(request):
#     # Build the path to your template dynamically
#     template_path = os.path.join('base.html')
#     template_full_path = os.path.join('templates', template_path)
#     print(template_full_path)
#     # Check if the template file exists
#     if not os.path.exists(template_full_path):
#         return HttpResponse("Template not found", status=404)

#     # Read the HTML content from the template file
#     with open(template_full_path, 'r', encoding='utf-8') as template_file:
#         html_content = template_file.read()

#     # Configure PDFKit options
#     options = {
#         'page-size': 'A4',
#         'margin-top': '0mm',
#         'margin-right': '0mm',
#         'margin-bottom': '0mm',
#         'margin-left': '0mm',
#     }

#     # Generate PDF using pdfkit
#     pdf_file = pdfkit.from_string(html_content, False, options=options)

#     # Create HTTP response with PDF content
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="output.pdf"'

#     return response