## Python uses docstring (triple quotes) for documentation 

## four different style of docString style 
## Google style (most beginers friendly)
## NumPy / SciPy style (for data analysis)
## Sphinx / restructure text (good for large projects)
## Type hints + DocString (modern Python approach)

### look up document - Python Functions Complete Guide.pdf (docs/python/references)

## Documentation best Practices 
# One line DocStrings for simple function 
def addnumbers(num1,num2):

    """Add two numbers and returns the result"""
    return num1 + num2

# Multi line DocStrings for complex functions 

def complex_function(data,config):
    """
    Process the data based on the provided configuration.

    Args:
        data (list): The input data to be processed.
        config (dict): Configuration settings for processing.

    Returns:
        list: Processed data.
    
    Raises:
        ValueError: If the data is not in the expected format.
    """
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")
    
    # Example processing logic
    return [item * config.get('multiplier', 1) for item in data]


def complex_calculation(data, config):
    """
    [One line summary - what the function does]
    
    [Blank line]
    
    [More detailed description explaining the purpose, algorithm,
    or any important implementation details that users should know]
    
    [Blank line]
    
    [Parameters section]
    
    [Returns section]
    
    [Raises section - if applicable]
    
    [Examples section - always helpful]
    
    [Notes/Warnings - if applicable]
    """
    pass

# Tools for documentation 

# use help function #help(my_function) => shows the docStrings

## IDE integration: Most IDE's will show docString as tooltips 
## when you hover over the function calls or use auto completion 

## Tools like Sphinx can automatically generate web documentation 
## from your docString 

## Quick documentation checklist 

# what does the function do? (one line summary)
# Why would some one use it (Purpose / context)
# How do you use it (Parameters and example)
# What do you return back (return value struture)
# What can go wrong (exception and edge cases) 
# Any special considerations (performance / side effect)
