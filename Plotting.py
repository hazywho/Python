import graph
graph.makeGraph_line(name="CompEvalHopane",show_output=False, show_dataframe=False,fileType=".png",
                     input_path=r"C:\Users\zanyi\OneDrive\Git hub\Python\Outside Work\Data\LineValues3.csv",
                     )#name output_path input_path show_output defaultx defaulty show_dataframe figsize title
graph.makeGraph_bar(show_output=False,show_dataframe=False,from_to=[0,44],fileType=".png",
                    input_path=r"C:\Users\zanyi\OneDrive\Git hub\Python\Outside Work\Data\BarValues21.csv",
                    name="CompEvalPhyBar")#from_to
graph.makeGraph_bar(show_output=False,show_dataframe=False,from_to=[45,78],name="CompEvalPhyBar2",
                    fileType=".png",input_path=r"C:\Users\zanyi\OneDrive\Git hub\Python\Outside Work\Data\BarValues21.csv")

