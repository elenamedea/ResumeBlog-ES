# Profile

profile_eng = """Data engineer who works across the full data lifecycle; from how data gets collected and what it means, to whether it can be trusted. With a research background and production experience in data engineering and AI automation, I bring rigour to messy real-world data problems and a track record of turning raw, heterogeneous inputs into reliable, governed, and actionable outputs."""
profile_de = """Als Dateningenieurin, decke ich den gesamten Datenlebenszyklus ab: von der Erfassung, über die Verifikation, und Analyse, bis hin zur Archivierung. Mit meinem wissenschaftlichen Hintergrund und praktischer Erfahrung in den Bereichen Datenengineering und KI-Automatisierung löse ich auch äußerst komplexe Datenprobleme mit hoher Präzision und kann auf eine Erfolgsbilanz bei der Umwandlung von heterogenen Rohdaten in zuverlässige, kontrollierte, umsetzbare Arbeitsergebnisse zurückblicken."""

profile_dict = {
    "English": profile_eng,
    "Deutsch": profile_de,
}

# Contact details
contact_keys = ["title", "email", "address", "linkedin", "github", "publications", "details"]
contact_eng = [
    "Contact details",
    "📧 Email",
    "📍 Address",
    "💼 LinkedIn",
    "🐈‍⬛🐙 GitHub",
    "📄 Publications",
    {
    "email": "elesyng@proton.me",
    "address": "Berlin, Germany",
    "linkedin": "linkedin.com/in/elenisyngelaki/",
    "github": "github.com/elenamedea",
    "publications": "researchgate.net/profile/Eleni-Syngelaki/publications",
    },
]
contact_de = [
    "Kontaktdaten",
    "📧 E-Mail",
    "📍 Adresse",
    "💼 LinkedIn",
    "🐈‍⬛🐙 GitHub",
    "📄 Publikationen",
    {
    "email": "elesyng@proton.me",
    "address": "Berlin, Deutschland",
    "linkedin": "linkedin.com/in/elenisyngelaki/",
    "github": "github.com/elenamedea",
    "publications": "researchgate.net/profile/Eleni-Syngelaki/publications",
    },
]

contact_dict = {
    "English": dict(zip(contact_keys, contact_eng)),
    "Deutsch": dict(zip(contact_keys, contact_de)),
}

# Work experience
work_experience_keys = ["title", "company", "period", "location", "keywords", "description"]
work_experience_eng = {
    "work_experience_1": [
        "Environmental Data Engineer",
        "eolos",
        "07/2024 – present",
        "Berlin, Germany",
        ":primary-background[*Python • Power BI • Mistral AI • n8n • Airtable • Git • Bash*]",
       """
        - Delivered 10+ client projects in Carbon Accounting and Data Architecture, acting as both technical lead and project manager for a 3-person team per engagement
        - Drove two Decarbonisation projects to production, one for a major European Enterprise with sites worldwide, by keeping technical decisions tied to actual business goals, to avoid scope drift
        - Redesigned Power BI reporting workflows, shipping dashboards two months ahead of schedule
        - Built multi-source data pipelines (APIs, SharePoint, documents) to ingest, clean, validate, and structure heterogeneous datasets; resolved >95% of client data issues without escalation
        - Owned team's end-to-end AI strategy, from surveying the team to understand real workflows, through tool selection, to delivering a company-wide roadmap and working implementations: agents, automations, and integrated workflows
        - Built a Mistral AI agent suite integrated with n8n workflows that cut the commercial team's time on lead generation, CRM enrichment, and contact scoring by ~50%; whole manual steps went away, not just got faster
    """,
    ],
    "work_experience_2": [
        "Research Consultant",
        "Unreal Estate GmbH",
        "03/2024 – 04/2024",
        "Berlin, Germany",
        ":primary-background[*Python • Streamlit • Docker • Git • Hugging Face spaces*]",
       """
        - Built an end-to-end Python pipeline for ingesting, cleaning, validating, and benchmarking a botanical dataset of 131 plant species, designed to scale to thousands of records
        - Deployed an open-source Streamlit EDA app, enabling three non-technical stakeholders to self-serve visual insights
    """,
    ],
    "work_experience_3": [
        "Data Engineering and Science Intern",
        "Spoty Labs",
        "05/2023 – 11/2023",
        "Berlin, Germany",
        ":primary-background[*Python • SQL • PostgreSQL • Streamlit • Docker • Git*]",
       """
        - Cut data errors by 60% in the first batch by introducing a validation framework with human-in-the-loop checks; error rate kept falling as the team adopted it
        - Designed and deployed an ETL pipeline for a counter-mapping web app; two spatial sources, transformed into analytics-ready datasets, loaded into a cloud-hosted PostgreSQL database
        - Modelled the relational schema and data contracts so the backend and application layers stayed in sync throughout the project
    """,
    ],
    "work_experience_4": [
        "Research associate",
        "Georg-August-Universität Göttingen",
        "02/2017 – 09/2021",
        "Göttingen, Germany",
        ":primary-background[*R • Python • Git • Bash • High Performance Computing (HPC) • Unix/Linux*]",
       """
        - Built reproducible bioinformatic pipelines on HPC for large-scale NGS and transcriptomic datasets
        - Awarded scholarship to the Summer Institute in Statistical Genetics, University of Washington, Seattle
    """,
    ],
}
work_experience_de = {
    "work_experience_1": [
        "Environmental Data Engineer",
        "eolos",
        "07/2024 – heute",
        "Berlin, Deutschland",
        ":primary-background[*Python • Power BI • Mistral AI • n8n • Airtable • Git • Bash*]",
       """
        - Umsetzung von mehr als zehn Projekten in den Bereichen CO₂-Bilanzierung, Datenarchitektur und Projektrealisierung, technische Leitung sowie Projektmanagement des Teams
        - Zwei Dekarbonisierungsprojekte, eins davon für einen großen europäischen Kunden (und Standorten weltweit), wurden bis zur Produktionsreife gebracht, hier wurden die technischen Entscheidungen stets anhand der tatsächlichen Geschäftsziele ausgerichtet, und so der schleichende Umfangszuwachs der Projekte begrenzt
        - Re-design von Power BI-Berichtsworkflows: Bereitstellung der Dashboards zwei Monate vor dem geplanten Abgabetermin
        - Erstellung von Datenpipelines aus verschiedenen Quellen (APIs, SharePoint, Dokumente) zur Erfassung, Bereinigung, Validierung und Strukturierung heterogener Datensätze; Lösung von mehr als 95 % der Datenbearbeitungsprobleme ohne weitere Kunden oder interne Nachfragen
        - Leitung der KI-Strategie des Teams, angefangen bei der Befragung des Teams zum Verständnis der tatsächlichen Arbeitsabläufe über die Auswahl der einzelnen Tools bis hin zur Erstellung einer unternehmensweiten Roadmap und der Umsetzung konkreter Lösungen mit: Agenten, Automatisierungen und integrierten Arbeitsabläufen
        - Entwicklung einer Mistral-KI-Agenten-Suite, die in n8n-Workflows integriert ist und den Zeitaufwand des Vertriebsteams für die Lead-Generierung, die CRM-Anreicherung und das Kontakt-Scoring um ca. 50 % reduziert hat; dabei wurden manuelle Schritte vollständig eliminiert und nicht nur beschleunigt
    """,
    ],
    "work_experience_2": [
        "Research Consultant",
        "Unreal Estate GmbH",
        "03/2024 – 04/2024",
        "Berlin, Deutschland",
        ":primary-background[*Python • Streamlit • Docker • Git • Hugging Face spaces*]",
       """
        - Entwicklung einer durchgängigen Python-Pipeline zur Erfassung, Bereinigung, Validierung und Leistungsbewertung eines botanischen Datensatzes mit 131 Pflanzenarten, der auf Tausende von Arten skalierbar ist
        - Bereitstellung einer Open-Source-EDA-App basierend auf Streamlit, die es den drei Stakeholdern ermöglicht Zusammenhänge anhand von Datenvisualisierungen selbständig zu analysieren
    """,
    ],
    "work_experience_3": [
        "Data Engineering and Science Intern",
        "Spoty Labs",
        "05/2023 – 11/2023",
        "Berlin, Deutschland",
        ":primary-background[*Python • SQL • PostgreSQL • Streamlit • Docker • Git*]",
       """
        - Reduzierung der Datenfehler um 60 % bereits in der ersten Charge durch Einführung eines Validierungsrahmens mit „Human-in-the-Loop“-Prüfungen; die Fehlerquote sank weiter, je mehr das Team das System einsetzte
        - Entwurf und Bereitstellung einer ETL-Pipeline für eine Web-App zur Gegenabbildung; zwei räumliche Quellen wurden in analysefähige Datensätze umgewandelt und in eine in der Cloud gehostete PostgreSQL-Datenbank geladen
        - Modellierung des relationalen Schemas und der Datenverträge, sodass Backend- und Anwendungsschicht während des gesamten Projekts synchron blieben
    """,
    ],
    "work_experience_4": [
        "Research associate",
        "Georg-August-Universität Göttingen",
        "02/2017 – 09/2021",
        "Göttingen, Deutschland",
        ":primary-background[*R • Python • Git • Bash • High Performance Computing (HPC) • Unix/Linux*]",
       """
        - Aufbau reproduzierbarer Bioinformatik-Pipelines mit HPC für große NGS- und Transkriptom-Datensätze
        - Stipendium für das Summer Institute in Statistical Genetics an der University of Washington, Seattle
    """,
    ],
}

work_experience_dict = {
    "English": {k: dict(zip(work_experience_keys, v)) for k, v in work_experience_eng.items()},
    "Deutsch": {k: dict(zip(work_experience_keys, v)) for k, v in work_experience_de.items()},
}

# Skills
# Note: the English CV carries one extra category (Product and Strategy)
# that the German version does not; the CV pages lay them out accordingly.
skills_keys = ["category", "input"]
skills_eng = {
    "skills_1": ["Programming Languages", "Python, R, SQL, Bash"],
    "skills_2": ["Data Engineering and Pipelines", "Pandas, NumPy, SQLAlchemy, pandera, PostgreSQL, MongoDB, Elasticsearch, Power Query, ETL/ELT design"],
    "skills_3": ["AI Engineering and Agentic Systems", "Mistral AI, Claude Code, n8n, LLM-powered agent design, Prompt engineering, Hugging Face"],
    "skills_4": ["Machine Learning", "Scikit-learn, TensorFlow/Keras, NLP, (Text) Classification, Regression, Time Series, Unsupervised Learning"],
    "skills_5": ["Data Visualisation and BI", "Power BI, Tableau, Streamlit, plotly, matplotlib, seaborn, PyGWalker, ggplot2"],
    "skills_6": ["Cloud, Infrastructure and DevOps", "AWS (EC2, RDS), Docker, Git, GitHub, GitLab, High Performance Computing (HPC), Unix/Linux, macOS"],
    "skills_7": ["Domain Knowledge", "Carbon accounting, Environmental data, Geospatial data, Bioinformatics"],
    "skills_8": ["Product and Strategy", "Roadmap definition, Stakeholder alignment, Requirements gathering, Cross-functional leadership, Agile delivery practices"],
    "skills_9": ["Languages", "English (fluent), German (C1), Greek"],
}
skills_de = {
    "skills_1": ["Programmiersprachen", "Python, R, SQL, Bash"],
    "skills_2": ["Data Engineering und Pipelines", "Pandas, NumPy, SQLAlchemy, pandera, PostgreSQL, MongoDB, Elasticsearch, Power Query, ETL/ELT-Design"],
    "skills_3": ["KI-Engineering und agentenbasierte Systeme", "Mistral AI, Claude, n8n, LLM-gestütztes Agenten-Design, Prompt-Engineering, Hugging Face"],
    "skills_4": ["Maschinelles Lernen", "Scikit-learn, TensorFlow/Keras, NLP, (Text-)Klassifizierung, Regression, Zeitreihen, unüberwachtes Lernen"],
    "skills_5": ["Datenvisualisierung und BI", "Power BI, Tableau, Streamlit, plotly, matplotlib, seaborn, PyGWalker, ggplot2"],
    "skills_6": ["Cloud, Infrastruktur und DevOps", "AWS (EC2, RDS), Docker, Git, GitHub, GitLab, High Performance Computing (HPC), Unix/Linux, macOS"],
    "skills_7": ["Fachwissen", "CO₂-Bilanzierung, Umweltdaten, Geodaten, Bioinformatik"],
    "skills_8": ["Sprachen", "Englisch (fließend), Deutsch (C1), Griechisch"],
}

skills_dict = {
    "English": {k: dict(zip(skills_keys, v)) for k, v in skills_eng.items()},
    "Deutsch": {k: dict(zip(skills_keys, v)) for k, v in skills_de.items()},
}

# Education
education_keys = ["studies", "institution", "period", "location"]
education_eng = {
    "education_1": [
        "Data Science Bootcamp",
        "Spiced Academy",
        "10/2022 – 01/2023",
        "Berlin, Germany",
    ],
    "education_2": [
        "Biology | Dr. rer. nat.",
        "Georg-August-Universität Göttingen",
        "02/2017 – 12/2021",
        "Göttingen, Germany",
    ],
    "education_3": [
        "Biology | Diploma",
        "Aristotle University of Thessaloniki",
        "09/2009 – 07/2015",
        "Thessaloniki, Greece",
    ],
}
education_de = {
    "education_1": [
        "Data Science Bootcamp",
        "Spiced Academy",
        "10/2022 – 01/2023",
        "Berlin, Deutschland",
    ],
    "education_2": [
        "Biology | Dr. rer. nat.",
        "Georg-August-Universität Göttingen",
        "02/2017 – 12/2021",
        "Göttingen, Deutschland",
    ],
    "education_3": [
        "Biology | Diplom",
        "Aristotle University of Thessaloniki",
        "09/2009 – 07/2015",
        "Thessaloniki, Griechenland",
    ],
}

education_dict = {
    "English": {k: dict(zip(education_keys, v)) for k, v in education_eng.items()},
    "Deutsch": {k: dict(zip(education_keys, v)) for k, v in education_de.items()},
}
