# 🎨 Design-o-Pedia

### Showcase Your Web & Graphic Design Projects

Design-o-Pedia is a **Streamlit-based web app** that allows web and graphic designers to submit and display their creative projects. This platform provides a simple and interactive way for designers to share their work, explore other projects, and access useful design resources.

## 🚀 Features

✅ **User-Friendly Interface:** Clean and intuitive layout for easy navigation.  
✅ **Project Submission Form:** Users can submit projects with details like name, title, category, description, and links (Behance, GitHub, Vercel, etc.).  
✅ **Projects Gallery:** Displays submitted projects in a structured table format.  
✅ **External Resources Section:** Quick access to platforms like Behance, GitHub, Vercel, and Streamlit.  
✅ **Responsive Design:** Uses `use_container_width=True` for seamless display on all screen sizes.  

## 🛠️ Tech Stack

- **Frontend & Backend:** Streamlit (Python-based framework)  
- **Data Handling:** Pandas (for managing project data)  
- **Image Processing:** PIL (for handling project images)  
- **Hosting:** Can be deployed on Streamlit Cloud  

## 📸 Screenshots

![Design-o-Pedia UI](https://source.unsplash.com/1000x400/?design,technology)

## ⚠️ Issues & Fixes

- **Deprecated `use_column_width` Warning:** Fixed by replacing it with `use_container_width`.  
- **Image Not Displaying Issue:** Ensured correct file path and added error handling.  
- **Project Submission UX Improvement:** Enhanced with structured form and success message.  

## 🔮 Future Enhancements

🔹 **Database Integration:** Store submitted projects persistently using Firebase, Supabase, or a local database.  
🔹 **User Authentication:** Allow users to log in and manage their project submissions.  
🔹 **Enhanced UI/UX:** Improve design with CSS styling and custom themes.  

## 💡 How to Run the Project

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/your-username/design-o-pedia.git
   cd design-o-pedia
   ```
2. **Install dependencies:**  
   ```bash
   pip install streamlit pandas pillow
   ```
3. **Run the app:**  
   ```bash
   streamlit run app.py
   ```

## 📜 License

This project is licensed under the MIT License.

---
💙 **Made with love using Streamlit**
