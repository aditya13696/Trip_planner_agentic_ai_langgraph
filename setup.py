from pathlib import Path
from setuptools import find_packages, setup

# Read requirements from requirements.txt, skipping comments and '-e .'
install_requires = []

with open("requirements.txt", encoding="utf-8") as f:
    install_requires = [
        line.strip()
        for line in f
        if line.strip()
        and not line.startswith("#")
        and not line.startswith("-e")
    ]

setup(
    name="AI_TRAVEL_PLANNER",  
    version="0.1.0",
    author="Aditya Sawant",
    author_email="sawant.adi79@gmail.com",
    description="Agentic AI application powered by LangChain, LangGraph, and FastAPI",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.10",
)