from pelican.plugins import pdf


AUTHOR = 'Bogdan Udaltsov'
SITENAME = "Bogdan's Blog"
SITEURL = "https://udaltsovrepo.github.io/resume_page.io"

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
PIC = "my_new_logo.jpeg"
THEME_STATIC_DIR = "theme"
DEFAULT_PAGINATION = 10

#Profile information
NAME                = 'Bogdan Udaltsov'
TAGLINE             = 'Senior Application Engineer'
CURRENT_LOCATION    = 'Poland, Siemianowice Slaskie' 

#sidebar links
EMAIL = 'udaltsov.en@gmail.com'
PHONE = '(+48) 721718956'
WEBSITE = ''
LINKEDIN = 'bogdan-udaltsov-024218198'
GITHUB = 'https://bitbucket.org/Bogdan3095'
TYPE_OF_COMM = "Email, Messengers"


TWITTER = ''
CSS_FILE = 'main-6.css'

CAREER_SUMMARY = """Possess experience of verification various IPs(traffic convertors, audio, memory subsystems) of different difficulties.
                    Had created qualitative verifications plans, which provided high standards of the functional verification.
                    Can write testbenches and all verification infrastructure from scratch in SystemVerilog, using UVM methodology.
                    Familiar with basic protocols, such as AMBA APB4, AXI, UART, SPI, I2C, MIPI SoundWire. Also possess knowledge of PCIe Gen5.
                    Have experience in synthesis with conformal analysis of the chip with writing SDC constraints on the design.
                    Have worked with simulators from leader vendors(Cadence, Synopsys, Mentor) and with its VIPs. CI/CD was performed in Jenkins, or using 
                    Cadence software, as Vmanager, with vsif scripts. Teamplayer, responsible and attentive to details.
                    Used to work on a high result. Had mentorship experience for the newcomers, and willinig to share my experience with team, for improving overall quality of 
                    our work. Constantly impoving my level of competency, by reading technical literature(computer architecture) and articles(DVcon). According to the last,
                    like to try new technics and observe their advantages/disadvantages.
                    Ready for the interesting projects and new challenges.
                    """


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

PROJECT_INTRO = ''

PROJECTS = [
    {   
        'position': 'Cadence Design Systems',
	    'title': "PCIe IP integaration and Verification",
	    'tagline':  """ 
                    Creation of the PCIe Gen5 subsystem, according to the customer needs, by integration inner IPs and providing addiotional
                    design stuff, with further verification and synthesis tasks.
                    """
	},
    {   
        'position': 'Cadence Design Systems',
	    'title': "Verification packages and open-source libs integration",
	    'tagline':  """ 
                        Creation of the verification libraries for the future reusability in the projects.
                        Observing and adoption of the open-source tools for further use with Cadence tools.
                        Creating new methodology for the acceleration of the simulation;
                    """
	},
    {   
        'position': 'Cadence Design Systems',
	    'title': "AXI4L2APB4 bridge",
	    'tagline':  """ 
                        Design and verification of the inner module for further use in the various projects.
                        Full design and verification cycle. Code linting for RTL was done with Jasper tools, 
                        regress and coverage annotation into the verification plan was done in the vManager, with
                        vsif files support. For the verification purposes various VIPs from VIPCAT were used.
                    """
	},
    {   
        'position': 'Cadence Design Systems',
	    'title': "Design and Verification reuse library",
	    'tagline':  """ Hub creation with design reuse modules and verification components for different purposes. 
                        Static website with sphinx engine was written with search
                        included(stork-search) and deployed on the Github pages.
                    """
	},
    {
        'position': 'Cadence Design Systems',
	    'title': "Memory integration testing",
	    'tagline':  """ Creating verification environment from scratch using uvm-methodology for performing synthesised memory modules of different types 
                        connectivity check and its  verification. All environment was written, 
                        according to the way, which was described in the article on the DVCON by Dave Rich form Siemens with abstract interface usage, 
                        for avoiding parametrization, and full incapsulation of the interface signals. 
                    """
	},
	{
        'position': 'Cadence Design Systems',
		'title': "Chip's synthesis",
		'tagline':  """ Performing synthesis of the chip, with advance nodes usage in the Genus software with LEC. Writing SDC constraints for the synthesis.
                        Preparing scripts for customer for different purposes, such as simulation, synthesis, formal checks, etc.
                    """
	},
	{
        'position': 'Cadence Design Systems',
		'title': 'Soundwire IP integration and verification',
		'tagline':  """ Integration of the IP into existing chip from the customer's side and providing verification according to the verification plan and existing 
                        verification environment. All legacy environment was written in an old-fashioned way, so it was rewritten in the UVM. 
                        Original testcases were debugged. 
                        For the verification VIP from Cadence was used, and verification was impelemented with legacy code support. 
                        For verification plan was used Vmanager, as for the regression with vsif scripts, simulator was xcelium.
                    """
	},

	{
        'position': 'Tecon MT',
		'title': 'Module Verification',
		'tagline':  """ Verification of the company's IP with its custom protocol. IP is an converter from one kind of traffic into AXI4 traffic 
                        with multiple modes. Full verification environment was written from scratch, using UVM methodology, 
                        according to the verification plan and responses from the meetups with the design team. 
                        For AXI4 load was used VIP from Synopsys. At the end it was put on the regress, using Jenkins, 
                        for collecting coverge and it's further observation. For verification plan creation and coverage annotation 
                        Verdi software was used, simulator was Synopsys VCS.
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
                        For PCB and Schematics Altium Designer was used. 
                        Various tools for microwave modelling: Microwave CST, Ansys HFSS, Keysight MWO.
                        In the majority Intel Altera FPGAs were used, so Quartus was chosen as software for firmware creation.
                        STM32 were used as top-priority MCs, for its firmwares Eclipse or Coocox IDE. At the end for 
                        adjustments and measurements different tools were used from multimeter to spectrum analyzers.
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
	'SystemVerilog',
    'UVM',
    'Functional Verification',
    'Computer Architecture',
    'Synthesis',
    'C',
    'C++',
    'Python',
    'SvUnit',
    'Natural Docs',
    'Sphinx',
    'PCIe',
    "Soundwire",
    "APB",
    "AXI"
]


EXPERIENCES = [
	{
		'job_title': 'Senior Application Engineer',
		'time': 'July 2024 - Present',
		'company': 'Cadence Design Systems',
                'details':  """ 
                                Creating a new methodologies for customers and inner use, 
                                according to the provided task.
                                Providing Design and verification services.
                                Mentor support for the new employees.
                            """
	},
	{
		'job_title': 'Application Engineer',
		'time': 'Nov 2022 - June 2024',
		'company': 'Cadence Design Systems',
                'details':  """ Providing Design and verification services for inner and customer's use.
                                In the majority, utilization of the Cadence tools, but it depend's on the customer.
                            """
	},
	{
		'job_title': "Module Verification Design Engineer",
		'time': 'Jul 2021 - Aug 2022',
		'company': 'Tecon MT',
                'details':  """ 
                                Module verification of the inner IPs, using Synopsys VCS and AXI VIP.
                            """
	},
	{
		'job_title': 'Senior RF Design Engineer',
		'time': 'Nov 2014 - Jul 2021',
		'company': 'Engineering center Era',
                'details':  """ Developing various equipments from idea to experimental model. 
                                Providing microwave simulation and modelling with various tools, 
                                PCB and mechanical design, adjusting for further putting on stream. 
                            """
	}
]

EDUCATIONS = [
	{
		'degree': 'Masters in Radio Engineering',
		'meta': 'Moscow Power Engineering Institute(Technical University)',
		'time': '2016 - 2020'
	},
	{
		'degree': 'B.E in Radio Engineering',
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
		'name': 'SystemVerilog Accelerated Verification with UVM',
		'author': 'Cadence Design Systems',
		'issued': 'Nov 2022'
	},
	{
		'name': 'SystemVerilog for Design and Verification v21.10',
		'author': 'Cadence Design Systems',
		'issued': 'Nov 2022'
	},
	{
		'name': 'SystemVerilog Assertions v5.1 Exam',
		'author': 'Cadence Design Systems',
		'issued': 'Feb 2020'
	},

	{
		'name': 'Basics of radio-location and navigation',
		'author': 'Moscow Aviation Institute (National Research University MAI)',
		'issued': 'Mar 2020'
	},
	{
		'name': 'Anti-jamming equipment design',
		'author': 'NPF Rodnik',
		'issued': 'Feb 2018'
	},

	{
		'name': 'Circuit design and signal integrity',
		'author': 'NPF Rodnik',
		'issued': 'Feb 2018'
	},
]

PLUGINS = [pdf,]
