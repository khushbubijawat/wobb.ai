def generate_summary(report_content):
    """Generates a summary section for the report."""
    summary = "Summary:\n"
    for section in report_content:
        summary += f"Section: {section['name']}\n"
        if 'content' in section:
            summary += f"Content: {section['content'][:200]}...\n"  # Summarize the content
        else:
            summary += "Content: Not available.\n"
    
    return summary
