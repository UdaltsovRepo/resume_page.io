AUTHOR = 'Bogdan Udaltsov'
SITENAME = "Bogdan's Blog"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

STATIC_PATHS = [
        ]

THEME = "./themes/resume"
PIC = "sitelogo.jpeg"

DEFAULT_PAGINATION = 10

#Profile information
NAME = 'Bogdan Udaltsov'
TAGLINE = 'Application engineer'

#sidebar links
EMAIL = 'udaltsov.en@gmail.com'
PHONE = '(+48) 721718956'
WEBSITE = 'empty'
LINKEDIN = 'empty'
GITHUB = 'empty'
TWITTER = ''
CSS_FILE = 'main-6.css'
CAREER_SUMMARY = """Practical and versatile Radio Engineer with work experience on different positions from technician 
                  to the senior engineer. Providing product from idea to practical realization, with mechanical parts 
                  and documentary. Adore to acquire new knowledge and solve modern tasks in engineering"""


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True



SKILLS = [
	{
		'title': 'SystemVerilog',
   		'level': '95'
   	},
  	{
  		'title': 'UVM',
   		'level': '90'
   	},
    {

  		'title': 'Python',
  		'level': '85'
  	},
    {
  		'title': 'C++',
  		'level': '80'
  	},
]

PROJECT_INTRO = 'You can list your side projects or open source libraries in this section. '

PROJECTS = [
    {   
        'position': 'Cadence Design Systems',
	    'title': "Design and Verification reuse library",
	    'tagline': """ Hub creation with design reuse modules for different purposes and verification components. Static website with sphinx engine was written with search
        included(stork-search) and deployed on the github pages.
        """
	},
    {
        'position': 'Cadence Design Systems',
	    'title': "Memory integration testing",
	    'tagline': """  Creating verification environment from scratch using uvm-methodology for performing connectivity check of the inner memory modules of
                        different types. In addition to this task, verification of these memories was added. All envirionment was written, 
                        according to the way, which was described in the article on the DVCON by Dave Rich form Siemens with abstract interface usage, for avoiding parametrization,
                        and full incapsulation of the interface signals. 
        """
	},
	{
        'position': 'Cadence Design Systems',
		'title': "Chip's synthesis",
		'tagline': """ Performing synthesys of the chip, with advance nodes usage in the Genus software with LEC. Writing SDC constraints for the synthesis.
                        Prepring scripts for customer for different purposes, such as simulation, synthesis, formal checks, etc.
        """
	},
	{
        'position': 'Cadence Design Systems',
		'title': 'Soundwire IP integration and verification',
		'tagline': """Integration of the IP into existing chip from the customer's side and providing verification according to the verification plan and existing 
        verification environment. All legacy environment was written in an old-fashioned way, so it was rewritten in the UVM. Original testcases were debugged. 
        For the verification VIP from Cadence was used, and verification was impelemented with legacy code support. 
        For verification plan was used Vmanager, as for the regression with vsif scripts, simulator was the xcelium.
        """
	},

	{
        'position': 'Tecon MT',
		'title': 'Module Verification',
		'tagline': """Verification of the company's IP with the custom protocol. IP is an converter from one kind of traffic into AXI4 traffic 
        with multiple modes. Full verification environment was written from scratch, using UVM methodology, according to the verification plan and resoponses from the meetups with the 
        design team. For AXI4 load was used VIP from Synopsys. At the end it was put on the regress, using Jenkins, 
        for collecting coverge and it's observation. For verification plan creation and coverage annotation Verdi software was used, simulator was Synopsys VCS.
        """
	},

	{
        'position': 'Pet-project',
		'title': 'IC_SPEC finder',
		'tagline': """  Program with GUI for downloading pdfs for the ICs, which are defined in the textfile.
                        Full code is written in python, with additional imported packages, such as
                        phantom, for browsing in hide mode, and selenium, for parsing webpage and trigger events.
        """
	},

	{
        'position': 'Pet-project',
		'title': 'Stand for measurements automation',
		'tagline': """  Automotive measurable stand, which consists of multiple software-measurable tools
                        such as generators, specter analyzers, scalar and vector analyzers, etc. plus the system
                        for configuring the measurable device, and the program for analyzing and parsing final data.
                        The main task of this project is to give to any user an opportunity to choose measurable device and 
                        scripts for basic measurements. After the completion of the measurements, automatically fill the xsl
                        template with parsed data and print it.
        """
	},

	{
        'position': 'Engineering Center Era',
		'title': 'RF-transcievers for various purposes',
		'tagline':  """ Equipment creation according to the technical specification, with multiple steps. 
                        For PCB and Shematics Altium Designer was used. 
                        Various tools for microwave modelling: Microwave CST, Ansys HFSS, Keysight MWO.
                        In the majority Intel Altera FPGAs were used, so Quartus was chosen as software for firmware creation.
                        STM32 were used as top-priority MCs, for its firmwares Eclipse or Coocox IDE. At the end for 
                        adjuastments and measurements different tools were used from multimeter to spectrum analyzers.
        """
	},

]


LANGUAGES = [
	{
		'name': 'Russian',
		'description': 'Native'
	},
	{
		'name': 'English',
		'description': 'Upper-Intermediate'
	},

	{
		'name': 'Polish',
		'description': 'Intermediate'
	},

	{
		'name': 'Belarusian',
		'description': 'Native'
	}
]


INTERESTS = [
	'Programming',
	'Reading',
    'Cycling',
]


EXPERIENCES = [
	{
		'job_title': 'Application Engineer',
		'time': 'Nov 2022 - Present',
		'company': 'Cadence Design Systems',
	},
	{
		'job_title': "Module verification design engineer",
		'time': 'Jul 2021 - Aug 2022',
		'company': 'Tecon MT',
	},
	{
		'job_title': 'Seniour RF design engineer',
		'time': 'Nov 2014 - Jul 2021',
		'company': 'Engineering center Era',
	}
]

EDUCATIONS = [
	{
		'degree': 'Masters in Radiotechnics',
		'meta': 'Moscow Power Engeineering Institute(Technical University)',
		'time': '2016 - 2020'
	},
	{
		'degree': 'B.E in Radiotechnics',
		'meta': 'Moscow State Institute of Radio Engineering, Electronics and Automation (Technical University)',
		'time': '2012 - 2016'
	},

]

COURSES = [

	{
		'name': 'SystemVerilog Assertions v5.1 Exam',
		'author': 'Cadence Design Systems',
		'issued': 'Feb 2023'
	},


	{
		'name': 'SystemVerilog Accelerated Verification with UVM v1.2.5 Exam',
		'author': 'Cadence Design Systems',
		'issued': 'Nov 2022'
	},
	{
		'name': 'SystemVerilog for Design and Verification v21.10 Exam',
		'author': 'Cadence Design Systems',
		'issued': 'Nov 2022'
	},
	{
		'name': 'SystemVerilog Assertions v5.1 Exam',
		'author': 'Cadence Design Systems',
		'issued': 'Feb 2020'
	},

	{
		'name': 'Basics of radiolocation and navigation',
		'author': 'Moscow Aviation Institute (National Research University MAI)',
		'issued': 'Mar 2020'
	},
	{
		'name': 'Anti-jamming equipment design (Altium Designer)',
		'author': 'NPF Rodnik',
		'issued': 'Feb 2018'
	},

	{
		'name': 'Circuit design and signal integrity (Altium Designer)',
		'author': 'NPF Rodnik',
		'issued': 'Feb 2018'
	},


]
