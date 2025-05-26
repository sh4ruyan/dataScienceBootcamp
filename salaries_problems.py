import pandas as pd

def findHighestOvertimePay(df):
    '''
    (DataFrame) -> int
    Takes a Pandas DataFrame and returns the highest value in the 
    'OvertimePay' column
    
    '''
    overtime_pay_list = df["OvertimePay"]
    max = -1
    exceptions_list = []
    for pay in overtime_pay_list:
        try:
            float_pay = float(pay)
            
            if (float_pay>max):
                max = float_pay

        except:
            exceptions_list.append(pay) 

    if (max == -1):
        print("There were no valid overtime pay values")

    return max 

def findJobTitle(df, name):
    target_index = df.loc[df["EmployeeName"]== name].index.to_list()[0] #just want the first one
    job_title_col_index = 2
    
    job_title = df.iloc[target_index, job_title_col_index]
    return job_title


def findEmployeeSalary(df, name)


def main():
    dataset_address = "C:\\Users\\Sharuyan Arumugam\\OneDrive\\Desktop\\Personal Projects\\Py_DS_ML_Bootcamp-master\\Salaries.csv"
    sal = pd.read_csv(dataset_address, low_memory=False)
    #Q1. Find the highest overtime pay 

    #findHighestOvertimePay(sal)
    
    #Q2. What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise
    #you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll).
    #print(findJobTitle(sal, "JOSEPH DRISCOLL"))

    #Q3. How much does JOSEPH DRISCOLL make(including benefits)?



main()
