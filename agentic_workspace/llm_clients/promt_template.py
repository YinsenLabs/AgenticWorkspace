from datetime import datetime


# Prompt template for calendar event creation from text input
def calendar_event_prompt(objective:str, persona: str = None, instructions: str = None, constraints: str = None, context: str = None, recap: str = None) -> str:
    """Prompt template for calendar event creation from text input

    Args:
        persona: The persona of the agent
        instructions: The instructions for the agent
        context: The context for the agent
        recap: The recap for the agent
        
    Returns:
        Formatted prompt string for the LLM to generate calendar event
    """

    #Default values
    if persona is None:
        persona = "calendar event creator"
    if instructions is None:
        instructions = "Create a calendar event from the given text"
    if constraints is None:
        constraints = "The event should be created in the next 30 days"
    if context is None:
        context = f"The user is a busy person who needs to create a calendar event"
    if recap is None:
        recap = "Re-emphasize the key aspects of the prompt, especially the instructions, constraints, etc."   

    # prompt template
    prompt = f"""
    <OBJECTIVE_AND_PERSONA>
    You are a {persona}. Your objective is to {objective}.
    </OBJECTIVE_AND_PERSONA>

    <INSTRUCTIONS>
    {instructions}
    </INSTRUCTIONS>

    ------------- Optional Components ------------

    <CONSTRAINTS>
    {constraints}
    </CONSTRAINTS>

    <CONTEXT>
    {context}, today is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    </CONTEXT>

    <RECAP>
    {recap}
    </RECAP>
    """
    return prompt
