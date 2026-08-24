def print_models(unprinted_designs, completed_models):
    """Simulates printing each 3D design until none are left."""
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Printing 3D model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Displays all the finished 3D printed models."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(f"- {model}")
