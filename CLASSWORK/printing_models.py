import printing_functions

designs_queue = ['phone case', 'robot pendant', 'dodecahedron dice']
finished_archive = []

printing_functions.print_models(designs_queue, finished_archive)
printing_functions.show_completed_models(finished_archive)