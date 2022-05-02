# json-editor-py
Watch the video demo: https://youtu.be/BbvcT_QJDS8

This is a JSON editor which can new, load, save and edit JSON files, in both code browser and content table views. 
	
The stand-alone editor tries to make the process of editting and transfering through JSON files intuitive, user-friendly, and easy to coordinate between tech and non-tech teams. 
	
Below is a screenshot, on the **left is JSON browser**, on the **right is visualized content table**. 
### ![image](https://user-images.githubusercontent.com/91817338/165051041-ce4ac3ac-080f-4c1e-b852-5babecf3ae6a.png)

# Prerequisites
### 1. PyQt5: used to create the user interface
	pip install PyQt5
### 2. Qt.py: used to load the .ui file directly
	pip install Qt.py
### 3. xmltodict: converting .xml to python dictionary
	pip install xmltodict

# Run it!
### 1. Download and unzip the JSON_Editor_Py package.
### 2. Run the main.py directly.
![image](https://user-images.githubusercontent.com/91817338/165061015-686cecb6-fd4d-47d8-8978-8f44d8d23dd7.png)

*** When saving the file, the editor will take the data in the left side(the JSON browser) to store in a file. So if you're making changes using the right side(the content table) or both sides, **remember to apply changes to the left side before saving**. 

# Features
### Create, Read, Save JSON files
![image](https://user-images.githubusercontent.com/91817338/165196956-56b55eaf-3041-4c1c-8aab-b2a677e07bec.png)

### Two-Way Editable, Two Clean Views
| JSON Browser | Content Table |
|-----|----|
| ![JSON Browser](https://user-images.githubusercontent.com/91817338/165064491-041a3869-99ea-4485-8c08-1909b7b49f7a.png) | ![Content Table](https://user-images.githubusercontent.com/91817338/165057632-90b170b4-3746-4eed-924d-177e628166f4.png) |

### One Button Expand or Collapse All
| Expand All | Collapse All |
|-----|----|
| ![Expand All](https://user-images.githubusercontent.com/91817338/165051692-ea129d28-adf0-4a6f-ae45-34275fb965b3.png) | ![Collapse All](https://user-images.githubusercontent.com/91817338/165051811-dd799748-11c2-4ef1-aeb4-45c400441388.png) |

### Super Intuitive UI by Simply Drag & Drop or Right Click
| Drag and Drop Entries | Create, Remove, Copy, Paste Entries |
|-----|----|
| ![Search](https://user-images.githubusercontent.com/91817338/165056643-5a8a8497-da0c-4812-a537-7da2e0dc1b08.png) | ![Search](https://user-images.githubusercontent.com/91817338/165056175-981e1d3b-ef3f-4538-95ca-53d9a8140c16.png) |

### Search for Keys
| Search | Search |
|-----|----|
| ![Search](https://user-images.githubusercontent.com/91817338/165058688-03a601ad-0845-4564-8b36-b50485229484.png) | ![Search](https://user-images.githubusercontent.com/91817338/165058942-f1c1fea9-cb8f-4fdc-9966-6d612c143825.png) |

### Sort by Keys or Values
| Sort by Keys | Sort by Values |
|-----|----|
| ![Sort by Keys](https://user-images.githubusercontent.com/91817338/165059511-68561154-a930-491e-a003-93d294a99171.png) | ![Sort by Values](https://user-images.githubusercontent.com/91817338/165059656-3f3fea7a-3d69-457d-b28d-48d310891512.png) |

### Import .xml Files and Convert to .json
| Original .xml Files | Import | Auto Convert |
|-----|----|----|
| ![Search](https://user-images.githubusercontent.com/91817338/165196460-ecc3edbc-52b5-4c6f-9452-1750458691e7.png) | ![Search](https://user-images.githubusercontent.com/91817338/165196584-7e9546c4-143d-4bef-bc74-3de9b695a978.png) | ![Search](https://user-images.githubusercontent.com/91817338/165196646-665eda0f-f605-49f6-87e7-2f94ac59be00.png) |

# Pathways
- [x] Save, Load and Create JSON files
- [x] Edit entries
- [x] Two-way Interface
- [x] Drag & Drop edit, Expand/Collapse, Search, Sort
- [x] Import and convert .xml files
- [ ] Drag & Drop to load files
- [ ] Custom Stylesheet
- [ ] Multi-tab editor

*Too busy to make updates thesedays, will continue adding features after May 13th, 2022.

# Reference
	https://github.com/AtsushiSakai/PyJSONViewer.git
	https://github.com/leixingyu/jsonEditor.git
	https://github.com/dridk/QJsonModel.git
