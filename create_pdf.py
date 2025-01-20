from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
html = HTML("./output/index.html")
font_config = FontConfiguration()
css_1 = CSS('output/theme/css/font-awesome.min.css', font_config=font_config)
css_2 = CSS('output/theme/css/bootstrap.min.css', font_config=font_config)
css_3 = CSS('output/theme/css/main-6.css', font_config=font_config)
css_4 = CSS(string=''' 
    @page {size: 340mm 680mm;} 
    @media print{
        *{
            text-shadow:none!important;
            color:#000!important;
            background:transparent!important;
            box-shadow:none!import  
        }
        a[href]:after {
            content: none !important;
        }
        .no-print, .no-print *
        {
            display: none !important;
        }
    }
''')
html.write_pdf(
    target="output/pdf/budaltso_resume.pdf", 
    stylesheets=[css_1, css_2, css_3, css_4],
    font_config=font_config,
    srgb=True,
    full_fonts=True,
    media_type='screen'
)

