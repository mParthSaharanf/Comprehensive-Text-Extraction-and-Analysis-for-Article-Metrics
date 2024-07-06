from SRC.data_extraction import data_ext
from SRC.utils import Col_Structure

if __name__ == "__main__":
    obj                                 = data_ext()
    str_obj                             = Col_Structure()
    obj1                                = obj.data_path()
    total_data,blank_list               = obj.data_extract()
    update_df                           = obj.Handdle_Blank_link(blank_list)
    combination                         = obj.merged(total_data,update_df)
    df                                  = str_obj.Col_Structure_Primary(total_data)