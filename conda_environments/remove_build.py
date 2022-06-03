
#%%
import yaml

with open(r'DS-CPU.yml') as file:
    package_list = yaml.load(file, Loader=yaml.FullLoader)
    for d in package_list["dependencies"]:
        if type(d) is str:
            print(d.split("="))
        else:
            # dictionary 
            # for p in d["pip"]:
                # print(p)
            pass
# %%
