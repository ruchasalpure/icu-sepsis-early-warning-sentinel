from crewai import Agent

icu_sepsis_early_warning_sentinel = Agent(
    role="Icu Sepsis Early Warning Sentinel",
    goal="Deliver high-precision autonomous Icu Sepsis Early Warning Sentinel operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
