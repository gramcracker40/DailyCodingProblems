import re
import os


class EnvParser:
    '''
    .env file management class

    def load(self, file=".env") --> Loads a regularly constructed .env file
    def replace_vars(self, new_file:str="parsed", vars:dict={}, load:bool=True)
            parses through the initialized .env file looking for any vars or substitute 
            delimiters. Once they are found, the method parses them accordingly. 
    
    
    '''
    
    def __init__(self, file=".env"):
        self.file = file


    @classmethod
    def load(self, file=".env"):
        '''
        Loads the specified .env file natively, only use if you do not have any 
        special characters to be parsed by this class like '{---}' or '$---$'
        ex: KEY=bvdifowk8f
        '''
        try:
            env_file = open(file, 'r')

            for line in env_file:
                temp = line.split('=')
                os.environ[temp[0]] = temp[1].replace("\n", "")
                
                print(f"Added! {os.environ[temp[0]]}")
  
        except FileNotFoundError as err:
            print(f"Error: FileNotFound --> {err}")
            return False

        return True


    def parse_load(self, new_file:str="parsed", vars:dict={}, 
                   load:bool=True, delete_new:bool=True) -> bool:
        '''
        PARSER
        Specify the vars you want to parse out and replace in the env file,
        this function will then open a new env file and rewrite the old with replaced vars. 
        
        vars ex: .env: --> KEY={Public}
           vars: --> {'Public': 'fbdsibfhisgbk3895i4te90jnfinsiJNIOU'}
           new_file.env --> KEY=fbdsibfhisgbk3895i4te90jnfinsiJNIOU

        substitute ex: KEY=8328Y4J
            CONNECTION_KEY=$KEY$:12345

            new_file.env --> KEY=8328Y4J
                             CONNECTION_KEY=8328Y4J:12345
        '''
        try:
            env_file = open(self.file, "r")
            env_list = [line.split("=") for line in env_file]
            env_file.close()

            parsed = []
            parsed_vars = {}
            for lines in env_list:
                if lines[1][0] != "{" and lines[1][0] != "$":
                    parsed_vars[lines[0]] = lines[1]
                    parsed.append(f"{lines[0]}={lines[1]}")
                elif lines[1][0] == "{": 
                    temp = vars[lines[1].replace('{', '').replace('}','')[:-1]]
                    parsed_vars[lines[0]] = temp
                    parsed.append(f"{lines[0]}={temp}\n")
                elif "$" in lines[1]: # there are referenced variables from above needing to be replaced
                    pattern = r"\$(.*?)\$"  # Anything between two '$' signs --> ex: $PERSON$
                    replace = re.findall(pattern, lines[1])
                    temp = lines[1]
                    
                    for var in replace:
                        temp = re.sub(pattern, parsed_vars[var].rstrip("\n"), temp, count=1) 
                    
                    parsed_vars[lines[0]] = temp
                    parsed.append(f"{lines[0]}={temp}")

            new_env = open(f"{new_file}.env", "w")
            new_env.writelines(parsed)
            new_env.close()

        except FileNotFoundError as err:
            print(f"Error: File Not Found --> {err}")
            return False
        
        self.replaced = f"{new_file}.env"

        if load:
            self.load_replaced(self, delete=delete_new)

        return True
    

    def load_replaced(self, delete=False):
        '''
        Takes the newly created env file and loads it into memory with the correct values
        You can also specify to delete the envfile directly following execution so your secrets
        are not lying dormant in a readable file. 
        '''
        try:
            replaced = open(self.replaced, 'r')
            env_list = [line.split("=") for line in replaced]

            for each in env_list:
                os.environ[each[0]] = each[1].rstrip("\n")

            replaced.close()
            if delete:
                os.remove(self.replaced)
        except FileNotFoundError as err:
            print(f"Error: FileNotFound --> {err}")
            return False

        return True

vars = {"PRIVATE": "cshuborhg8w4ijnjfsj0", "PUBLIC": "bsu8ferij4nfidsmvosjd90fjw0jni"}

# test = EnvParser(file=".env")
# replaced = test.replace_vars(vars=vars)
# load = test.load_replaced(delete=True)

# print(replaced)
# print(load)

EnvParser.load()

print(os.environ["PUBKEY"])