"""You have to implement a VersionManager class.

It should accept an optional parameter that represents the initial version. The input will be in one of the following formats:
 "{MAJOR}", "{MAJOR}.{MINOR}", or "{MAJOR}.{MINOR}.{PATCH}". More values may be provided after PATCH but they should be ignored.
   If these 3 parts are not decimal values, an exception with the message "Error occured while parsing version!" should be thrown.
     If the initial version is not provided or is an empty string, use "0.0.1" by default.

This class should support the following methods, all of which should be chainable (except release):

major() - increase MAJOR by 1, set MINOR and PATCH to 0
minor() - increase MINOR by 1, set PATCH to 0
patch() - increase PATCH by 1
rollback() - return the MAJOR, MINOR, and PATCH to their values before the previous major/minor/patch call, 
or throw an exception with the message "Cannot rollback!" if there's no version to roll back to. Multiple calls to rollback()
 should be possible and restore the version history

release() - return a string in the format "{MAJOR}.{MINOR}.{PATCH}" """

class VersionManager:

    def __init__ (self,version="0.0.1"):
        """Initialise all self variables"""
    
        self.OG_version=""
        self.version=version
        self.versions_checked=[]
        self.history=[]
        self.Major=""
        self.Minor=""
        self.Patch=""
        self.current_ver=""
        self.first=True
        self.make_version()

    def check_ver(self):
        """Ensures defualt ver and creates ver from input"""
    
        if self.version=="":
            self.versions_checked=[0,0,1]
        
        else:
                max_index=len(self.version)
                self.version=list(self.version)
                index=0
                decimals=0
                numbers=["0","1","2","3","4","5","6","7","8","9"]
                listy=""
                self.versions_checked=[]
                for char in self.version:
                    if char not in numbers:
                        if char==".":
                            decimals+=1
                            self.versions_checked.append(listy)
                            listy=""
                            index+=1
                            
                        else:
                            raise Exception("Error occured while parsing version!")
                        
                    elif char in numbers:
                        listy+=char
                        index+=1
                        
                    if index==max_index:
                        self.versions_checked.append(listy)
                        
                    if decimals==3:
                        break

        return self
    
    def check_for_enough(self):
        """Allows for inputs shorted than full ver"""
    
        if len(self.versions_checked) >=1:
            self.versions_checked.append("0")
            self.versions_checked.append("0")
            
        elif len(self.versions_checked) ==2:
            self.versions_checked.append("0")

    def make_version(self):
        """runs checks, applies to returnable variable and ensure initial ver added to history"""
    
        self.check_ver()
        self.check_for_enough()    
        self.Major=self.versions_checked[0]
        self.Minor=self.versions_checked[1]
        self.Patch=self.versions_checked[2]
        self.current_ver= "{}.{}.{}".format(self.Major,self.Minor,self.Patch)

        if self.first ==True:
            
            self.history.append(self.current_ver)
            self.OG_version=self.current_ver

        self.first=False
        return self

    def major(self):
        """Increments major, resets others and adds to history"""
    
        self.Major=int(self.Major)+1
        self.Minor="0"
        self.Patch="0"
        self.current_ver= "{}.{}.{}".format(self.Major,self.Minor,self.Patch)
        self.history.append(self.current_ver)
        return self

    def minor(self):
        """Increments minor, resets patch and adds to history"""
        
        self.Minor=int(self.Minor)+1
        self.Patch="0"
        self.current_ver= "{}.{}.{}".format(self.Major,self.Minor,self.Patch)
        self.history.append(self.current_ver)
        return self

    def patch(self):
        """Increments patch, resets patch and adds to history"""
        
        self.Patch=int(self.Patch)+1
        self.current_ver= "{}.{}.{}".format(self.Major,self.Minor,self.Patch)
        self.history.append(self.current_ver)
        return self

    def rollback(self):
        """Rollsback though ver history, raises exception if cannot"""

        if len(self.history)==1:
                raise Exception ("Cannot rollback!")    
            
        else:

            try:    
                    self.history.pop(-1)
                    self.current_ver=self.history[-1]
                    self.version=self.current_ver
                    self.make_version()
            
            except: 
                raise Exception ("Cannot rollback!")
        
        return self
        
    def release(self):
        """Returns current ver"""
        
        return self.current_ver
    
"""
Top answer:

class VersionManager:
    
    def __init__(self, version=None):
        if not version: version='0.0.1'
        self.__memory = []
        try:
            arr = [*map(int,version.split('.')[:3])] + [0,0,0]
        except:
            raise Exception("Error occured while parsing version!")
        del arr[3:]
        self.__version = arr if any(arr) else [0,0,1]
    
    def release(self):
        return '.'.join(map(str, self.__version))

    def rollback(self):
        if not self.__memory: raise Exception("Cannot rollback!")
        self.__version = self.__memory.pop()
        return self
        
    def __update(self, i):
        self.__memory.append([*self.__version])
        self.__version[i] += 1
        self.__version[i+1:] = [0] * (len(self.__version)-1-i)
        return self
    
    def major(self): return self.__update(0)
    def minor(self): return self.__update(1)
    def patch(self): return self.__update(2)







"""