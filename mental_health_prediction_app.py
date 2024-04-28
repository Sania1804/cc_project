import numpy as np
import pickle
import streamlit as st



pickle_in = open('cc_model.sav','rb') 
model = pickle.load(pickle_in) 
#creating a function

def health_prediction(input_data):

    input_new = np.asarray(input_data)
    input_array = input_new.reshape(1, -1)
    prediction = model.predict(input_array)
    if (prediction[0] == 1):
        return """
                You have Anxiety.Anxiety is a mental health condition characterised by excessive worry, fear, or nervousness about future events or situations.\n
                It often involves physical symptoms like increased heart rate, muscle tension, and restlessness. Treatment for anxiety can include therapy, such as cognitive-behavioural therapy (CBT), medication, lifestyle changes, and relaxation techniques.\n
                The most effective approach often depends on the severity of the anxiety and the individual's specific needs, and a mental health professional can provide guidance on the best treatment plan.\n
                [Reference Video](https://youtu.be/9mPwQTiMSj8?si=tkaZ40cu20cLtjNu)\n\n
                [Reference Article](https://newsinhealth.nih.gov/2016/03/understanding-anxiety-disorders)
                """
    elif (prediction[0] == 2):
        return """
                You have Depression.Depression is a mental health disorder characterised by persistent feelings of sadness, hopelessness, and a lack of interest or pleasure in activities. 
                It can also be accompanied by symptoms such as changes in appetite, sleep disturbances, fatigue, and difficulty concentrating. Depression can have a significant impact on a person's daily life and functioning.\n
                It is a complex condition that can result from a combination of genetic, biological, environmental, and psychological factors. Treatment options often include therapy, medication, and lifestyle changes. If you or someone you know is struggling with depression, it's important to seek help from a mental health professional.\n
                [Reference Video](https://youtu.be/z-IR48Mb3W0?si=5V8YxrbxuXTcN3Se)\n\n
                [Reference Article](https://www.ncbi.nlm.nih.gov/books/NBK430847/)
                """
    elif (prediction[0] == 3):
        return """
               You have Stress.Stress is a natural physiological and psychological response to challenging or demanding situations. It's your body's way of preparing to face a threat or pressure. Stress can be caused by a variety of factors, including work, relationships, financial issues, or major life changes. \n When you experience stress, your body releases stress hormones like cortisol and adrenaline, which can trigger a "fight or flight" response.
               In small or short-term doses, stress can be beneficial as it helps you stay alert and focused.\n However, chronic or excessive stress can have negative effects on your physical and mental health. It can lead to symptoms such as anxiety, irritability, sleep disturbances, and, in the long term, more serious health issues like cardiovascular problems or mental health disorders. Managing stress through relaxation techniques, exercise, time management, and seeking support when needed is important for overall well-being.\n
                [Reference Video](https://youtu.be/1BBiaxOxXas?si=lVXUCIqY7N5NjpFN)\n\n
                [Reference Article](https://www.medicalnewstoday.com/articles/145855#types)
                """
    elif (prediction[0] == 4):
        return """
                    You have Loneliness. Loneliness is the emotional state of feeling isolated, disconnected, or alone, often accompanied by a sense of emptiness and a lack of meaningful social connections.\n
                    It can be a distressing and painful experience, even when a person is surrounded by others, as it's more about the quality of social interactions rather than the quantity. 
                    Loneliness can result from various factors, including social isolation, the absence of close relationships, or a perceived lack of understanding and emotional support. It can have negative effects on mental and physical health. \n
                    Addressing loneliness may involve seeking social connections, engaging in activities, and talking to friends, family, or a mental health professional to combat these feelings.\n
                    [Reference Video](https://youtu.be/n3Xv_g3g-mA?si=cfU5SLQnIEPtIo-E) \n\n
                    [Reference Article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6179015/)
                    """
    else:
        return "You are Normal. It's great to hear that you're feeling well!"
 
def main():
   st.title('Mental Health Prediction App') 
   
   st.write("Type 1 - Yes & 0 - No")

   feeling_nervous = st.text_input('Are you currently feeling nervous?')
   panic = st.text_input('Have you experienced panic recently?')
   breathing_rapidly = st.text_input('Are you breathing rapidly more than usual?')
   sweating = st.text_input('Do you find yourself sweating excessively?')
   trouble_in_concentration= st.text_input('Are you having trouble concentrating?')
   having_trouble_in_sleeping = st.text_input('Do you have trouble sleeping at night?')
   having_trouble_with_work = st.text_input('Are you struggling with your work or tasks?')
   hopelessness = st.text_input('Do you ever feel a sense of hopelessness?')
   anger = st.text_input('Are you frequently experiencing anger?')
   over_react = st.text_input('Do you tend to overreact to situations?')
   change_in_eating = st.text_input('Have you noticed a change in your eating habits?')
   suicidal_thought = st.text_input('Have you had any suicidal thoughts?')
   feeling_tired = st.text_input('Are you feeling tired most of the time?')
   close_friend = st.text_input('Do you have a close friend to confide in?')
   social_media_addiction = st.text_input('Are you addicted to social media?')
   weight_gain = st.text_input('Have you experienced weight gain recently?')
   material_possessions = st.text_input('Do material possessions hold significant importance for you?')
   introvert = st.text_input('Would you consider yourself an introvert?')
   popping_up_stressful_memory= st.text_input('Do stressful memories keep popping up for you?')
   having_nightmares= st.text_input('Are you having nightmares while sleeping?')
   avoids_people_or_activities= st.text_input('Do you tend to avoid people or certain activities?')
   feeling_negative = st.text_input('Are you generally feeling negative about things?')
   trouble_concentrating = st.text_input('Are you having trouble concentrating on tasks?')
   blamming_yourself = st.text_input('Do you often blame yourself for various situations or problems?')
   
   daignosis = ''
   
   if st.button("Click to check your result"):
       daignosis = health_prediction([feeling_nervous,panic,breathing_rapidly,sweating,trouble_in_concentration,
                                      having_trouble_in_sleeping,having_trouble_with_work,hopelessness,anger,over_react,change_in_eating,suicidal_thought,
                                      feeling_tired,close_friend,social_media_addiction,weight_gain,material_possessions,introvert,
                                      popping_up_stressful_memory,having_nightmares,avoids_people_or_activities,feeling_negative,trouble_concentrating,
                                      blamming_yourself])
   st.success(daignosis)   


if __name__ == '__main__':
    main()
    

