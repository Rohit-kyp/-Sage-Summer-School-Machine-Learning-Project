"""
Day-2 
We Are Spliting ouur complete pdf text to some samll pices.
and these small pieces are know as chunks.

"""
import pickle
from langchain_text_splitters import RecursiveCharacterTextSplitter

#Task-1 Load the extrected .txt file in read mode
def load_file():
    with open ('extracted_text.txt') as file:
        text = file.read()
        return text
    

#Task-2 Chunking the row text from extrected.text file
def split_text(text):
    splitter = RecursiveCharacterTextSplitter (chunk_size = 500 ,chunk_overlap = 50)
    chunks = splitter.split_text(text)
    return chunks


#print Top 3 chunks
def view_chunks(chunks):
    for index, value in enumerate(chunks):
        print(f'chunk {index}: {value}' )
        print('-----------------------------')


#Saving all the Chunks in a .txt file name as chunks.txt
def save_chunks(chunks):
    with open('chunks.txt','w') as file:
        for index, value in enumerate(chunks):
            file.write(f'chunk {index} : {value}\n')
            file.write('-----------------------')

# Task-3 save the chunks in .pkl format
def save_chunks(chunks):
    with open('chunks.pkl','wb') as file:
        pickle.dump(chunks,file)
    print('File Save Sucessfully in .pkl format')



text = load_file()
chunks = split_text(text)
save_chunks(save_chunks)
print(len(chunks))