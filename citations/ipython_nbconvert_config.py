c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['*.ipynb']
c.NbConvertApp.export_format = 'latex'
c.Exporter.template_file = 'citations'
c.SphinxTransformer.author = 'Fernando Perez and Brian E. Granger'
