# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'


# %%
import sys
with open(sys.argv[1],'r') as f:
    rawinput=str(f.read())
    mylist=rawinput.split()

# %%
months=int(mylist[0])
death=int(mylist[1])


# %%
memory=[0,1,1]
for i in range(2,death):
    x = memory[-1] + memory[-2]
    memory.append(int(x))
memory.append(memory[-1] + memory[-2] - 1)


# %%
for i in range(death+1,months):
    tmp= memory[-1] + memory[-2] - memory[(-death-1)]
    memory.append(tmp)


# %%
print(memory[-1])


