
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def open_file_get_data(filetoopen):
    return open(filetoopen).readlines()

def data_collection(data,column):
    """Collects data by column from csv"""

    compileddata = []
    label = data[0].split('\t')[column]

    for i in data:
        compileddata.append(i.split('\t')[column])
    del compileddata[0]

    return label, compileddata


def qual_count(qual_data):
    """Counts qualitative data"""
    qual_data_count_dict = dict()
    for i in qual_data:
        if i not in qual_data_count_dict:
            qual_data_count_dict[i] = 1
        else:
            qual_data_count_dict[i] = qual_data_count_dict[i] + 1

        qual_data_count = list()

    for i in qual_data_count_dict:
        qual_data_count.append(qual_data_count_dict[i])

    return qual_data_count_dict,list(qual_data_count_dict.keys()), qual_data_count,

def make_qual_bar_graph(fileinfo,row_x,row_y,title,savename,xlabel=None,ylabel=None):
    datelabel, datedata = data_collection(fileinfo,row_x)
    FC_label, FC_data = data_collection(fileinfo,row_y)
    qualitative_count, quantit_cat, qual_data_count = qual_count(FC_data)

    y_pos = np.arange(len(quantit_cat))
    plt.bar(y_pos, qual_data_count, align='center', alpha=0.5)
    plt.xticks(y_pos, quantit_cat)
    plt.xticks(fontsize=8,rotation=30)
    plt.title(title)
    #plt.tight_layout()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.autoscale()
    plt.savefig(savename,bbox_inches = "tight")
    plt.clf()
    plt.cla()


def quan_count(data):
    pass


def make_quan_bar_graph(fileinfo, row_x,row_y,title,savename,xlabel=None,ylabel=None):
    datelabel, datedata = data_collection(fileinfo, row_x)
    FC_label, FC_data = data_collection(fileinfo, row_y)
    for i in range(len(FC_data)):
        try:
            FC_data[i] = int(FC_data[i])
        except:
            FC_data[i] = float(FC_data[i])
    y_pos = np.arange(len(FC_data))
    plt.plot(FC_data, alpha=0.5)
    #plt.xticks(y_pos, quantit_cat)
    plt.xticks(fontsize=8, rotation=0)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.autoscale()
    plt.savefig(savename, bbox_inches="tight")
    plt.clf()
    plt.cla()


if __name__ == '__main__':
    fileinfo = open_file_get_data('stats.csv')

    make_qual_bar_graph(fileinfo,1,2,"Who FCs in Goblins?","Who_FCs.png", xlabel="Fleet Commanders",ylabel="Times they FC'd")
    make_qual_bar_graph(fileinfo, 1, 0, "Types of Fleets", "Fleet_Types.png",ylabel="Numbers of \nthose fleets")
    make_quan_bar_graph(fileinfo, 1, 4,"Ships killed in Goblin Fleets","ShipsKilled.png",xlabel="Fleet",ylabel="Ships Killed")
    make_quan_bar_graph(fileinfo, 1, 5, "Ship Value killed in Goblin Fleets", "ShipValueKilled.png", xlabel="Fleet", ylabel="ISK Value Killed (Mil ISK)")
    make_quan_bar_graph(fileinfo, 1, 6, "Ships lost in Goblin Fleets", "Shipslost.png", xlabel="Fleet", ylabel="ISK Value Lost (Mil ISK)")
    make_quan_bar_graph(fileinfo, 1, 7, "Ship Value lost in Goblin Fleets", "ShipValueLost.png", xlabel="Fleet", ylabel="ISK Value Killed (Mil ISK)")
    make_quan_bar_graph(fileinfo, 1, 8, "Fleet Efficiency", "Efficiency.png", xlabel="Fleet", ylabel="Efficiency")

    # datelabel, datedata = data_collection(fileinfo,1)
    # FC_label, FC_data = data_collection(fileinfo,2)
    # qualitative_count, quantit_cat, qual_data_count = qual_count(FC_data)
    #
    # y_pos = np.arange(len(quantit_cat))
    # plt.bar(y_pos, qual_data_count, align='center', alpha=0.5)
    # plt.xticks(y_pos, quantit_cat)
    # plt.xticks(rotation=45)
    # plt.title("Who FC's what fleets?")
    # plt.savefig('FC_who_fcs.png')






    pass