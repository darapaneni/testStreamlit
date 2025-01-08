import streamlit as st


import streamlit as st

# Sidebar for navigation
st.sidebar.title("Landmark Consulting Services")
selection = st.sidebar.radio("Go to", ["About Us", "Services", "Internships", "Live Project"])

# About Us Tab
if selection == "About Us":
    st.title("About Us")
    st.write("""
    Welcome to the LCS Online Assessment Platform Development project. Our objective is to develop an advanced online assessment platform for evaluating candidates’ technical and non-technical skills. 
    The platform will feature custom tests, real-time coding assessments, and detailed analytics, leveraging the Python technology stack for development.
    """)

# Services Tab
elif selection == "Services":
    st.title("Services")
    st.write("""
    Our platform offers a range of services including:
    - **On-Job Internships:** Provide opportunity to interns to contribute to our live projects where interns get to work on real-world problems.
    - **Technology solutions to real estate:** Property documentation etc.
    - **Legal solutions:** Help in Civil litigations, Criminal cases, family disputes, Legal documentations, Legal opinions.
    """)

# Internships Tab
elif selection == "Internships":
    st.title("Internships")
    st.write("""
    Join our team as an intern and gain hands-on experience in:
    - Generative AI engineering
    - ChatGPT tools technology
    - LLM expertise
    - AI Agents development
    - Backend and frontend development
    """)

# Live Project Tab
elif selection == "Live Project":
    st.title("LCS Online Assessment Platform Development")
    # Objective
    st.header("Objective")
    st.write("""
    - Develop an advanced online assessment platform for evaluating candidates’ technical and non-technical skills.
    - The platform will feature custom tests, real-time coding assessments, and detailed analytics, leveraging the Python technology stack for development.
    - It will incorporate GitHub Copilot, Large Language Models (LLMs), Retrieval-Augmented Generation (RAGs), Prompt Engineering techniques, and Azure OpenAI for enhanced functionality.
    """)

    # Stakeholders
    st.header("Stakeholders")
    st.write("""
    - **Project Sponsor:** Internal or external client requiring the platform.
    - **Development Team:** Backend engineers, frontend developers, AI specialists, and QA specialists.
    - **End Users:** Recruiters, hiring managers, and job candidates.
    """)

    # Scope
    st.header("Scope")

    # Functional Requirements
    st.subheader("Functional Requirements")
    st.write("""
    - **User Management:**
    - User registration and authentication.
    - Role-based access control for admins, recruiters, and candidates.
    - **Test Creation and Customization:**
    - Allow recruiters to create custom tests.
    - Predefined question bank categorized by domain and difficulty.
    - **Support for multiple question types:**
    - Multiple choice questions (MCQs).
    - Coding challenges.
    - Essay-style questions.
    - **Real-Time Coding Assessments:**
    - Integrated code editor supporting Python and other programming languages.
    - Evaluate code for correctness, efficiency, and style.
    - Execution and testing within a secure sandbox environment.
    - **Test Delivery and Proctoring:**
    - Generate unique test links for candidates.
    - Real-time proctoring using webcam and screen monitoring (optional).
    - Timed assessments with automatic submission on timeout.
    - **Results and Analytics:**
    - Detailed score breakdown per candidate.
    - Comparison of multiple candidates’ performance.
    - Exportable reports (PDF, Excel).
    - **Notifications and Alerts:**
    - Email notifications for test invites and result availability.
    - Alerts for incomplete assessments or suspected malpractice.
    - **Admin Panel:**
    - Manage users, tests, and question banks.
    - Monitor platform usage and analytics.
    """)

    # Non-Functional Requirements
    st.subheader("Non-Functional Requirements")
    st.write("""
    - **Performance:**
    - Support up to 1,000 concurrent users.
    - Response time of <2 seconds for most interactions.
    - **Scalability:**
    - Modular design for scaling compute resources during high demand.
    - **Security:**
    - Secure data transmission with SSL/TLS encryption.
    - AES-256 encryption for sensitive data storage.
    - OAuth2 for authentication and authorization.
    - Regular vulnerability scanning and patching.
    - **Reliability:**
    - Uptime of 99.9%.
    - Automated backups with daily frequency.
    """)

    # Technology Stack
    st.subheader("Technology Stack")
    st.write("""
    - **Backend:**
    - Framework: Django (Python).
    - Database: PostgreSQL.
    - Authentication: Django REST Framework with OAuth2.
    - **Frontend:**
    - Framework: React.js (optional for admin and test-taker UI).
    - Communication: REST APIs (Django REST Framework).
    - **Sandbox Environment:**
    - Library: Docker for code execution sandbox.
    - Tools: Pytest for evaluating Python coding challenges.
    - **Proctoring:**
    - Library: OpenCV for face detection and screen monitoring (optional).
    - **AI and ML Integration:**
    - GitHub Copilot for code suggestions.
    - Azure OpenAI for natural language processing and AI-driven insights.
    - LLMs and RAGs for enhanced question generation and evaluation.
    - Prompt Engineering techniques for adaptive testing.
    - **DevOps:**
    - Server: Gunicorn with Nginx for deployment.
    - Containerization: Docker.
    - CI/CD: GitHub Actions or Jenkins.
    - **Other Libraries:**
    - Pandas and Matplotlib for result analytics.
    - Celery with Redis for background task management (e.g., sending emails).
    """)

    # Key Milestones and Deliverables
    st.header("Key Milestones and Deliverables")
    st.write("""
    - **Week 1-4:**
    - Requirements gathering and design documentation.
    - Database schema design.
    - First technical article to publish in medium.com
    - **Week 5-8:**
    - Development of core features (user management, test creation, result analytics).
    - Implementation of REST APIs.
    - Second technical article to publish in medium.com
    - **Week 9-12:**
    - Integration of real-time code execution environment.
    - Initial test deployment and proctoring integration.
    - Third technical article to publish in medium.com
    - **Week 13-16:**
    - Frontend development (admin and candidate dashboards).
    - QA and security testing.
    - Fourth technical article to publish in medium.com
    - **Week 17-20:**
    - Deployment on cloud infrastructure.
    - User training and final delivery.
    - Fifth technical article to publish in medium.com
    """)

    # Budget and Resources
    st.header("Budget and Resources")
    st.write("""
    - **Team:**
    - Generative AI engineers
    - ChatGPT tools technologists
    - LLM experts
    - AI Agents developers
    - Backend developers (Python/Django).
    - Frontend developers (React.js).
    - DevOps engineers.
    - QA specialists.
    - **Infrastructure:**
    - Cloud hosting (AWS, Azure, or GCP).
    - Docker and CI/CD tools.
    """)

# Run the Streamlit app
if __name__ == "__main__":
    st.write(" ")

