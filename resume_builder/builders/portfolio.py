class PortFolioExtractor:

    def __init__(self, param_str_basePath:str):
        self._str_basePortfolioPath = param_str_basePath
    
    def extract(self, local_str_companyName:str, local_str_projectName:str):
        
        with open(f"{self._str_basePortfolioPath}//{local_str_companyName}//{local_str_projectName}.md") as local_file_extractor:
            return local_file_extractor.read()