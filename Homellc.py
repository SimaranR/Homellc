{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b8546b40",
   "metadata": {},
   "source": [
    "# Home Price Index"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "15885abf",
   "metadata": {},
   "source": [
    "<center>\n",
    "<h1 style=\"font-size: 40px; font-family: serif;\">Import Libraries</h1>\n",
    "</center>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9befe98d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Downloading streamlit-1.29.0-py2.py3-none-any.whl (8.4 MB)\n",
      "     ---------------------------------------- 8.4/8.4 MB 12.2 MB/s eta 0:00:00\n",
      "Collecting blinker<2,>=1.0.0\n",
      "  Downloading blinker-1.7.0-py3-none-any.whl (13 kB)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Collecting validators<1,>=0.2\n",
      "  Downloading validators-0.22.0-py3-none-any.whl (26 kB)\n",
      "Collecting tzlocal<6,>=1.1\n",
      "  Downloading tzlocal-5.2-py3-none-any.whl (17 kB)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (1.23.5)\n",
      "Collecting rich<14,>=10.14.0\n",
      "  Downloading rich-13.7.0-py3-none-any.whl (240 kB)\n",
      "     ------------------------------------- 240.6/240.6 kB 15.4 MB/s eta 0:00:00\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Collecting pyarrow>=6.0\n",
      "  Downloading pyarrow-14.0.1-cp310-cp310-win_amd64.whl (24.6 MB)\n",
      "     --------------------------------------- 24.6/24.6 MB 10.4 MB/s eta 0:00:00\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (2.28.1)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (22.0)\n",
      "Collecting protobuf<5,>=3.20\n",
      "  Downloading protobuf-4.25.1-cp310-abi3-win_amd64.whl (413 kB)\n",
      "     ------------------------------------- 413.4/413.4 kB 25.2 MB/s eta 0:00:00\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (9.4.0)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (1.5.3)\n",
      "Requirement already satisfied: importlib-metadata<7,>=1.4 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (4.11.3)\n",
      "Collecting tenacity<9,>=8.1.0\n",
      "  Downloading tenacity-8.2.3-py3-none-any.whl (24 kB)\n",
      "Collecting altair<6,>=4.0\n",
      "  Downloading altair-5.2.0-py3-none-any.whl (996 kB)\n",
      "     ------------------------------------- 996.9/996.9 kB 31.8 MB/s eta 0:00:00\n",
      "Collecting cachetools<6,>=4.0\n",
      "  Downloading cachetools-5.3.2-py3-none-any.whl (9.3 kB)\n",
      "Collecting pydeck<1,>=0.8.0b4\n",
      "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
      "     ---------------------------------------- 4.8/4.8 MB 16.1 MB/s eta 0:00:00\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (4.4.0)\n",
      "Collecting gitpython!=3.1.19,<4,>=3.0.7\n",
      "  Downloading GitPython-3.1.40-py3-none-any.whl (190 kB)\n",
      "     ---------------------------------------- 190.6/190.6 kB ? eta 0:00:00\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: toolz in c:\\users\\asus\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: colorama in c:\\users\\asus\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Collecting gitdb<5,>=4.0.1\n",
      "  Downloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
      "     ---------------------------------------- 62.7/62.7 kB ? eta 0:00:00\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from importlib-metadata<7,>=1.4->streamlit) (3.11.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2022.7)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2022.12.7)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.14)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Collecting pygments<3.0.0,>=2.13.0\n",
      "  Downloading pygments-2.17.2-py3-none-any.whl (1.2 MB)\n",
      "     ---------------------------------------- 1.2/1.2 MB 18.6 MB/s eta 0:00:00\n",
      "Collecting markdown-it-py>=2.2.0\n",
      "  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)\n",
      "     ---------------------------------------- 87.5/87.5 kB 5.2 MB/s eta 0:00:00\n",
      "Collecting tzdata\n",
      "  Downloading tzdata-2023.3-py2.py3-none-any.whl (341 kB)\n",
      "     ---------------------------------------- 341.8/341.8 kB ? eta 0:00:00\n",
      "Collecting smmap<6,>=3.0.1\n",
      "  Downloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Collecting mdurl~=0.1\n",
      "  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
      "Installing collected packages: validators, tzdata, tenacity, smmap, pygments, pyarrow, protobuf, mdurl, cachetools, blinker, tzlocal, pydeck, markdown-it-py, gitdb, rich, gitpython, altair, streamlit\n",
      "  Attempting uninstall: tenacity\n",
      "    Found existing installation: tenacity 8.0.1\n",
      "    Uninstalling tenacity-8.0.1:\n",
      "      Successfully uninstalled tenacity-8.0.1\n",
      "  Attempting uninstall: pygments\n",
      "    Found existing installation: Pygments 2.11.2\n",
      "    Uninstalling Pygments-2.11.2:\n",
      "      Successfully uninstalled Pygments-2.11.2\n",
      "Successfully installed altair-5.2.0 blinker-1.7.0 cachetools-5.3.2 gitdb-4.0.11 gitpython-3.1.40 markdown-it-py-3.0.0 mdurl-0.1.2 protobuf-4.25.1 pyarrow-14.0.1 pydeck-0.8.1b0 pygments-2.17.2 rich-13.7.0 smmap-5.0.1 streamlit-1.29.0 tenacity-8.2.3 tzdata-2023.3 tzlocal-5.2 validators-0.22.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "abe33d3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9502d7f2",
   "metadata": {},
   "source": [
    "\n",
    "# Creating Dataframe\n",
    "<span id=\"Importdata\"></span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ffc05ce6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>DATE</th>\n",
       "      <th>CSUSHPISA</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1987-01-01</td>\n",
       "      <td>63.965</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1987-02-01</td>\n",
       "      <td>64.424</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1987-03-01</td>\n",
       "      <td>64.736</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1987-04-01</td>\n",
       "      <td>65.132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1987-05-01</td>\n",
       "      <td>65.563</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>436</th>\n",
       "      <td>2023-05-01</td>\n",
       "      <td>302.566</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>437</th>\n",
       "      <td>2023-06-01</td>\n",
       "      <td>304.593</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>438</th>\n",
       "      <td>2023-07-01</td>\n",
       "      <td>306.767</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>439</th>\n",
       "      <td>2023-08-01</td>\n",
       "      <td>309.155</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>440</th>\n",
       "      <td>2023-09-01</td>\n",
       "      <td>311.175</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>441 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           DATE  CSUSHPISA\n",
       "0    1987-01-01     63.965\n",
       "1    1987-02-01     64.424\n",
       "2    1987-03-01     64.736\n",
       "3    1987-04-01     65.132\n",
       "4    1987-05-01     65.563\n",
       "..          ...        ...\n",
       "436  2023-05-01    302.566\n",
       "437  2023-06-01    304.593\n",
       "438  2023-07-01    306.767\n",
       "439  2023-08-01    309.155\n",
       "440  2023-09-01    311.175\n",
       "\n",
       "[441 rows x 2 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(r\"Home Price Index.csv\")\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d34e7a02",
   "metadata": {},
   "source": [
    "<center>\n",
    "<h1 style=\"font-size: 40px; font-family: serif;\">Data Preprocessing,</h1>\n",
    "</center>\n",
    "<span id=\"Datatcleaning\"></span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ff1fb585",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>DATE</th>\n",
       "      <th>CSUSHPISA</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1987-01-01</td>\n",
       "      <td>63.965</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1987-02-01</td>\n",
       "      <td>64.424</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1987-03-01</td>\n",
       "      <td>64.736</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1987-04-01</td>\n",
       "      <td>65.132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1987-05-01</td>\n",
       "      <td>65.563</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         DATE  CSUSHPISA\n",
       "0  1987-01-01     63.965\n",
       "1  1987-02-01     64.424\n",
       "2  1987-03-01     64.736\n",
       "3  1987-04-01     65.132\n",
       "4  1987-05-01     65.563"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b9a5ae06",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>DATE</th>\n",
       "      <th>CSUSHPISA</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>436</th>\n",
       "      <td>2023-05-01</td>\n",
       "      <td>302.566</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>437</th>\n",
       "      <td>2023-06-01</td>\n",
       "      <td>304.593</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>438</th>\n",
       "      <td>2023-07-01</td>\n",
       "      <td>306.767</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>439</th>\n",
       "      <td>2023-08-01</td>\n",
       "      <td>309.155</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>440</th>\n",
       "      <td>2023-09-01</td>\n",
       "      <td>311.175</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           DATE  CSUSHPISA\n",
       "436  2023-05-01    302.566\n",
       "437  2023-06-01    304.593\n",
       "438  2023-07-01    306.767\n",
       "439  2023-08-01    309.155\n",
       "440  2023-09-01    311.175"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1a76d5cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DATE          object\n",
       "CSUSHPISA    float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "44e225c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 441 entries, 0 to 440\n",
      "Data columns (total 2 columns):\n",
      " #   Column     Non-Null Count  Dtype  \n",
      "---  ------     --------------  -----  \n",
      " 0   DATE       441 non-null    object \n",
      " 1   CSUSHPISA  441 non-null    float64\n",
      "dtypes: float64(1), object(1)\n",
      "memory usage: 7.0+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "95c3b483",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CSUSHPISA</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>441.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>141.910490</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>61.191389</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>63.965000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>82.194000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>141.029000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>178.767000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>311.175000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        CSUSHPISA\n",
       "count  441.000000\n",
       "mean   141.910490\n",
       "std     61.191389\n",
       "min     63.965000\n",
       "25%     82.194000\n",
       "50%    141.029000\n",
       "75%    178.767000\n",
       "max    311.175000"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a91384f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DATE         0\n",
       "CSUSHPISA    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find out null values\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1d147cef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DATE\n",
      "['1987-01-01' '1987-02-01' '1987-03-01' '1987-04-01' '1987-05-01'\n",
      " '1987-06-01' '1987-07-01' '1987-08-01' '1987-09-01' '1987-10-01'\n",
      " '1987-11-01' '1987-12-01' '1988-01-01' '1988-02-01' '1988-03-01'\n",
      " '1988-04-01' '1988-05-01' '1988-06-01' '1988-07-01' '1988-08-01'\n",
      " '1988-09-01' '1988-10-01' '1988-11-01' '1988-12-01' '1989-01-01'\n",
      " '1989-02-01' '1989-03-01' '1989-04-01' '1989-05-01' '1989-06-01'\n",
      " '1989-07-01' '1989-08-01' '1989-09-01' '1989-10-01' '1989-11-01'\n",
      " '1989-12-01' '1990-01-01' '1990-02-01' '1990-03-01' '1990-04-01'\n",
      " '1990-05-01' '1990-06-01' '1990-07-01' '1990-08-01' '1990-09-01'\n",
      " '1990-10-01' '1990-11-01' '1990-12-01' '1991-01-01' '1991-02-01'\n",
      " '1991-03-01' '1991-04-01' '1991-05-01' '1991-06-01' '1991-07-01'\n",
      " '1991-08-01' '1991-09-01' '1991-10-01' '1991-11-01' '1991-12-01'\n",
      " '1992-01-01' '1992-02-01' '1992-03-01' '1992-04-01' '1992-05-01'\n",
      " '1992-06-01' '1992-07-01' '1992-08-01' '1992-09-01' '1992-10-01'\n",
      " '1992-11-01' '1992-12-01' '1993-01-01' '1993-02-01' '1993-03-01'\n",
      " '1993-04-01' '1993-05-01' '1993-06-01' '1993-07-01' '1993-08-01'\n",
      " '1993-09-01' '1993-10-01' '1993-11-01' '1993-12-01' '1994-01-01'\n",
      " '1994-02-01' '1994-03-01' '1994-04-01' '1994-05-01' '1994-06-01'\n",
      " '1994-07-01' '1994-08-01' '1994-09-01' '1994-10-01' '1994-11-01'\n",
      " '1994-12-01' '1995-01-01' '1995-02-01' '1995-03-01' '1995-04-01'\n",
      " '1995-05-01' '1995-06-01' '1995-07-01' '1995-08-01' '1995-09-01'\n",
      " '1995-10-01' '1995-11-01' '1995-12-01' '1996-01-01' '1996-02-01'\n",
      " '1996-03-01' '1996-04-01' '1996-05-01' '1996-06-01' '1996-07-01'\n",
      " '1996-08-01' '1996-09-01' '1996-10-01' '1996-11-01' '1996-12-01'\n",
      " '1997-01-01' '1997-02-01' '1997-03-01' '1997-04-01' '1997-05-01'\n",
      " '1997-06-01' '1997-07-01' '1997-08-01' '1997-09-01' '1997-10-01'\n",
      " '1997-11-01' '1997-12-01' '1998-01-01' '1998-02-01' '1998-03-01'\n",
      " '1998-04-01' '1998-05-01' '1998-06-01' '1998-07-01' '1998-08-01'\n",
      " '1998-09-01' '1998-10-01' '1998-11-01' '1998-12-01' '1999-01-01'\n",
      " '1999-02-01' '1999-03-01' '1999-04-01' '1999-05-01' '1999-06-01'\n",
      " '1999-07-01' '1999-08-01' '1999-09-01' '1999-10-01' '1999-11-01'\n",
      " '1999-12-01' '2000-01-01' '2000-02-01' '2000-03-01' '2000-04-01'\n",
      " '2000-05-01' '2000-06-01' '2000-07-01' '2000-08-01' '2000-09-01'\n",
      " '2000-10-01' '2000-11-01' '2000-12-01' '2001-01-01' '2001-02-01'\n",
      " '2001-03-01' '2001-04-01' '2001-05-01' '2001-06-01' '2001-07-01'\n",
      " '2001-08-01' '2001-09-01' '2001-10-01' '2001-11-01' '2001-12-01'\n",
      " '2002-01-01' '2002-02-01' '2002-03-01' '2002-04-01' '2002-05-01'\n",
      " '2002-06-01' '2002-07-01' '2002-08-01' '2002-09-01' '2002-10-01'\n",
      " '2002-11-01' '2002-12-01' '2003-01-01' '2003-02-01' '2003-03-01'\n",
      " '2003-04-01' '2003-05-01' '2003-06-01' '2003-07-01' '2003-08-01'\n",
      " '2003-09-01' '2003-10-01' '2003-11-01' '2003-12-01' '2004-01-01'\n",
      " '2004-02-01' '2004-03-01' '2004-04-01' '2004-05-01' '2004-06-01'\n",
      " '2004-07-01' '2004-08-01' '2004-09-01' '2004-10-01' '2004-11-01'\n",
      " '2004-12-01' '2005-01-01' '2005-02-01' '2005-03-01' '2005-04-01'\n",
      " '2005-05-01' '2005-06-01' '2005-07-01' '2005-08-01' '2005-09-01'\n",
      " '2005-10-01' '2005-11-01' '2005-12-01' '2006-01-01' '2006-02-01'\n",
      " '2006-03-01' '2006-04-01' '2006-05-01' '2006-06-01' '2006-07-01'\n",
      " '2006-08-01' '2006-09-01' '2006-10-01' '2006-11-01' '2006-12-01'\n",
      " '2007-01-01' '2007-02-01' '2007-03-01' '2007-04-01' '2007-05-01'\n",
      " '2007-06-01' '2007-07-01' '2007-08-01' '2007-09-01' '2007-10-01'\n",
      " '2007-11-01' '2007-12-01' '2008-01-01' '2008-02-01' '2008-03-01'\n",
      " '2008-04-01' '2008-05-01' '2008-06-01' '2008-07-01' '2008-08-01'\n",
      " '2008-09-01' '2008-10-01' '2008-11-01' '2008-12-01' '2009-01-01'\n",
      " '2009-02-01' '2009-03-01' '2009-04-01' '2009-05-01' '2009-06-01'\n",
      " '2009-07-01' '2009-08-01' '2009-09-01' '2009-10-01' '2009-11-01'\n",
      " '2009-12-01' '2010-01-01' '2010-02-01' '2010-03-01' '2010-04-01'\n",
      " '2010-05-01' '2010-06-01' '2010-07-01' '2010-08-01' '2010-09-01'\n",
      " '2010-10-01' '2010-11-01' '2010-12-01' '2011-01-01' '2011-02-01'\n",
      " '2011-03-01' '2011-04-01' '2011-05-01' '2011-06-01' '2011-07-01'\n",
      " '2011-08-01' '2011-09-01' '2011-10-01' '2011-11-01' '2011-12-01'\n",
      " '2012-01-01' '2012-02-01' '2012-03-01' '2012-04-01' '2012-05-01'\n",
      " '2012-06-01' '2012-07-01' '2012-08-01' '2012-09-01' '2012-10-01'\n",
      " '2012-11-01' '2012-12-01' '2013-01-01' '2013-02-01' '2013-03-01'\n",
      " '2013-04-01' '2013-05-01' '2013-06-01' '2013-07-01' '2013-08-01'\n",
      " '2013-09-01' '2013-10-01' '2013-11-01' '2013-12-01' '2014-01-01'\n",
      " '2014-02-01' '2014-03-01' '2014-04-01' '2014-05-01' '2014-06-01'\n",
      " '2014-07-01' '2014-08-01' '2014-09-01' '2014-10-01' '2014-11-01'\n",
      " '2014-12-01' '2015-01-01' '2015-02-01' '2015-03-01' '2015-04-01'\n",
      " '2015-05-01' '2015-06-01' '2015-07-01' '2015-08-01' '2015-09-01'\n",
      " '2015-10-01' '2015-11-01' '2015-12-01' '2016-01-01' '2016-02-01'\n",
      " '2016-03-01' '2016-04-01' '2016-05-01' '2016-06-01' '2016-07-01'\n",
      " '2016-08-01' '2016-09-01' '2016-10-01' '2016-11-01' '2016-12-01'\n",
      " '2017-01-01' '2017-02-01' '2017-03-01' '2017-04-01' '2017-05-01'\n",
      " '2017-06-01' '2017-07-01' '2017-08-01' '2017-09-01' '2017-10-01'\n",
      " '2017-11-01' '2017-12-01' '2018-01-01' '2018-02-01' '2018-03-01'\n",
      " '2018-04-01' '2018-05-01' '2018-06-01' '2018-07-01' '2018-08-01'\n",
      " '2018-09-01' '2018-10-01' '2018-11-01' '2018-12-01' '2019-01-01'\n",
      " '2019-02-01' '2019-03-01' '2019-04-01' '2019-05-01' '2019-06-01'\n",
      " '2019-07-01' '2019-08-01' '2019-09-01' '2019-10-01' '2019-11-01'\n",
      " '2019-12-01' '2020-01-01' '2020-02-01' '2020-03-01' '2020-04-01'\n",
      " '2020-05-01' '2020-06-01' '2020-07-01' '2020-08-01' '2020-09-01'\n",
      " '2020-10-01' '2020-11-01' '2020-12-01' '2021-01-01' '2021-02-01'\n",
      " '2021-03-01' '2021-04-01' '2021-05-01' '2021-06-01' '2021-07-01'\n",
      " '2021-08-01' '2021-09-01' '2021-10-01' '2021-11-01' '2021-12-01'\n",
      " '2022-01-01' '2022-02-01' '2022-03-01' '2022-04-01' '2022-05-01'\n",
      " '2022-06-01' '2022-07-01' '2022-08-01' '2022-09-01' '2022-10-01'\n",
      " '2022-11-01' '2022-12-01' '2023-01-01' '2023-02-01' '2023-03-01'\n",
      " '2023-04-01' '2023-05-01' '2023-06-01' '2023-07-01' '2023-08-01'\n",
      " '2023-09-01'] \n",
      "\n",
      "CSUSHPISA\n",
      "[ 63.965  64.424  64.736  65.132  65.563  66.071  66.507  66.938  67.33\n",
      "  67.739  68.107  68.506  68.858  69.263  69.64   69.977  70.426  70.889\n",
      "  71.354  71.799  72.24   72.635  73.071  73.466  73.946  74.382  74.778\n",
      "  75.086  75.306  75.479  75.657  75.835  76.056  76.283  76.521  76.705\n",
      "  76.897  77.053  77.201  77.278  77.297  77.258  77.139  77.008  76.85\n",
      "  76.699  76.37   76.185  75.915  75.734  75.57   75.565  75.765  75.993\n",
      "  76.082  76.109  76.192  76.074  76.014  76.087  76.156  76.278  76.346\n",
      "  76.399  76.332  76.264  76.231  76.239  76.376  76.559  76.674  76.784\n",
      "  76.837  76.867  76.936  77.037  77.243  77.429  77.613  77.795  77.942\n",
      "  78.148  78.326  78.591  78.727  78.856  78.988  79.222  79.423  79.595\n",
      "  79.781  79.919  80.065  80.15   80.296  80.427  80.528  80.599  80.661\n",
      "  80.704  80.785  80.938  81.11   81.307  81.482  81.619  81.737  81.834\n",
      "  81.953  82.194  82.421  82.61   82.752  82.929  83.086  83.257  83.377\n",
      "  83.553  83.722  83.956  84.181  84.453  84.623  84.862  85.08   85.331\n",
      "  85.573  85.851  86.147  86.633  87.093  87.615  88.003  88.442  88.879\n",
      "  89.364  89.845  90.31   90.786  91.258  91.717  92.199  92.712  93.208\n",
      "  93.672  94.218  94.785  95.344  95.975  96.592  97.219  97.863  98.523\n",
      "  99.154  99.845 100.551 101.339 102.127 102.922 103.678 104.424 105.054\n",
      " 105.768 106.538 107.382 108.302 109.14  109.846 110.5   111.109 111.652\n",
      " 112.164 112.796 113.491 114.167 114.812 115.31  115.857 116.455 117.144\n",
      " 117.845 118.687 119.611 120.724 121.813 122.888 123.83  124.78  125.735\n",
      " 126.67  127.624 128.461 129.355 130.148 130.884 131.735 132.649 133.777\n",
      " 134.969 136.294 137.531 138.794 140.179 141.646 143.192 145.059 146.593\n",
      " 148.186 149.85  151.338 152.633 154.179 155.75  157.527 159.33  161.288\n",
      " 163.344 165.812 167.501 169.351 171.19  172.86  174.442 176.438 178.028\n",
      " 179.68  180.91  182.321 183.287 184.364 184.329 184.156 183.507 183.068\n",
      " 182.594 182.798 183.198 183.609 184.139 184.517 184.598 184.15  183.01\n",
      " 181.6   180.254 179.111 178.116 177.558 176.624 175.147 174.342 173.132\n",
      " 171.541 170.053 168.338 166.659 165.017 163.566 161.987 160.308 158.327\n",
      " 156.142 153.619 151.507 150.015 148.66  147.949 147.694 148.09  148.41\n",
      " 148.278 148.025 147.85  148.134 147.929 147.396 145.631 145.859 146.403\n",
      " 146.394 145.721 144.991 143.916 143.019 142.531 142.173 142.06  141.521\n",
      " 140.35  139.981 140.01  139.905 139.862 139.73  139.309 138.668 137.952\n",
      " 137.152 136.674 136.607 136.533 137.904 139.154 140.155 141.029 141.669\n",
      " 142.279 142.908 143.6   144.585 145.503 146.827 147.785 149.963 151.519\n",
      " 152.85  154.199 155.604 156.965 158.227 159.242 160.074 160.994 161.927\n",
      " 162.526 163.086 163.393 163.66  164.062 164.577 165.215 165.905 166.642\n",
      " 167.335 168.05  168.634 169.13  169.8   170.298 170.881 171.469 172.13\n",
      " 172.937 173.828 174.792 175.739 176.543 177.274 177.649 178.164 178.767\n",
      " 179.43  180.082 180.832 181.852 182.824 183.751 184.759 185.722 186.805\n",
      " 187.315 187.993 188.725 189.617 190.51  191.452 192.665 193.759 194.804\n",
      " 195.955 197.172 198.315 199.232 199.966 200.658 201.425 202.233 202.913\n",
      " 203.689 204.349 205.112 205.669 206.156 206.539 206.862 207.066 207.513\n",
      " 208.136 208.649 209.287 210.093 210.904 211.791 212.787 213.933 214.994\n",
      " 215.864 216.402 216.812 216.98  217.616 219.378 222.391 225.837 229.753\n",
      " 233.208 236.486 239.56  242.369 245.465 249.07  253.407 258.358 262.82\n",
      " 266.845 270.377 273.725 277.21  281.342 285.924 291.153 296.445 300.573\n",
      " 303.762 304.724 303.879 301.473 299.353 298.873 298.269 297.413 297.03\n",
      " 297.537 298.637 300.213 302.566 304.593 306.767 309.155 311.175] \n",
      "\n"
     ]
    }
   ],
   "source": [
    "for i in df.columns:\n",
    "    print(i)\n",
    "    print(df[i].unique(),'\\n')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b15ead1",
   "metadata": {},
   "source": [
    "<center>\n",
    "<h1 style=\"font-size: 40px; font-family: serif;\">Visualize the Data</h1>\n",
    "</center>\n",
    "<span id=\"Datatcleaning\"></span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "af09dbc1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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f9i+fTvPPPPMDT9mVlYWp06dokKFCldtExUVxd69e+nWrRsuLi4Fuu6xY8d44IEHmD17NkuWLGHo0KG8/fbbDB8+3NImJSWFrl27EhMTw0cffcTy5ct57733qFy5MsnJyZZ2w4cPZ8yYMXTp0oXFixfz8ccfs2/fPlq1akVMTMx1a2nZsiU//PADkyZNYteuXdf8IAm5QzWnTZvGK6+8wg8//ICPjw933XXXTYWBy1JTU2nfvj1ff/01o0eP5pdffuHZZ59l5syZ9OnTJ19YXrx4MdOnT+fFF1/kt99+o23bttd9jOzs7Hy3Kz3nQ4cO0apVK/bt28cHH3zAwoULqV27NoMHD2bKlCn52j/33HPExsYyc+ZM3nnnHVatWsX9999Pv3798PT0ZN68eYwfP57Zs2fz3HPP5bnvzb6HV3L5g/U/v3czMzPp06cPnTp14scff+Tll1++6v0HDx7Mk08+SdOmTVmwYAHz58+nT58+eULzG2+8wf3330/t2rX59ttvmT17NsnJybRt25b9+/ffUN0A/fr1Izw8nB9++IH//ve/zJ07l6eeespy3jAM7rzzTkuYWLRoES1atKBnz575rrV//36aNm3K3r17eeedd1iyZAm33347o0ePtjx/Jycnvv32W2JjY3nkkUeA3ID54IMPYhgG8+bNw9bW9qr1Ll++nICAAEuo/TcXFxe6devG3r17iY6OpkGDBjRs2JAZM2bkaztz5kz8/f3p1atXgev/pwkTJhAZGcknn3zCzz//jL+//zVe6RuXlZXF3Xffze23386PP/5Iz549mTBhAs899xyDBg3ikUceYdGiRURERDB48GC2bdtmuW90dDTNmjXjt99+48UXX+SXX35h6NChTJ48mWHDhhVLvSLlmjW7z0SkZDt//rzRpk0bAzAAw97e3mjVqpUxefJkIzk5OU/bpKQko0+fPkZERIQBGM8999x1r1+lShWjV69eRlZWlpGVlWWcOHHCGDRokAEYzzzzzFXvt3HjRgMw/vvf/97Q88rJyTGysrKMWbNmGba2tsbFixcNwzCMrVu3GoCxePHiq953w4YNBmC88847eY6fPn3acHZ2NsaPH3/dxz969KhRt25dy+vq7OxsdO7c2Zg2bZqRmZmZpy1gBAQEGElJSZZj0dHRho2NjTF58mTLscvD1k6cOGE5VpAhgpMnTzZsbGzyDXf7/vvvDcBYtmxZnlo8PT0tr9f1tG/f3vIcr3b759Cy++67z3B0dDQiIyPzXKdnz56Gi4uLkZCQYBjG/w+v6t27d552Y8aMMQBj9OjReY7feeedho+Pj+Xrm30PL7/WGzduNLKysozk5GRjyZIlRoUKFQx3d3cjOjraMAzD8r381Vdf5bvGv9+bNWvWGIAxceLEqz5uZGSkYWdnZ4waNSrP8eTkZCMwMNDo37//Neu+0rC0l156yQCMKVOm5Gn7+OOPG05OTpbht7/88osBGO+//36edq+//nq+97F79+5GpUqVjMTExDxtR44caTg5OeX5/lmwYIEBGO+9957x4osvGjY2Nsbvv/9+zedhGIbh5ORktGjR4pptnn32WQMwNm3aZBiGYXzwwQcGYBw6dMjS5uLFi4ajo6Mxbty4Qtd/+fW82nDfa7nWEMHL5/7880/LscvfSz/88IPlWFZWllGhQgUDMLZv3245fuHCBcPW1tYYO3as5djw4cMNNzc349SpU3ke63//+58BGPv27Sv0cxCRq1MPlohcla+vL2vXrmXLli28+eab9O3bl8OHDzNhwgTq1avH+fPnLW3vv/9+zp07x65du3jttdd44403ePHFFy3nz5w5g8lkyvcX5GXLlmFvb4+9vT1hYWF8++23jBo1itdee61In8uOHTvo06cPvr6+2NraYm9vz8MPP0xOTo5lmFP16tXx9vbm2Wef5ZNPPrlij8CSJUswmUw89NBDeXpkAgMDadCggWVYj2EY+XptLqtWrRq7du1i9erVvPzyy3Tp0oUtW7YwcuRIWrZsSXp6ep7H7NixI+7u7pavAwIC8Pf3v+4wyoJYsmQJdevW5bbbbstTa/fu3a+4klmnTp3w9vYu8PWrVavGli1b8t1WrFiRr+3KlSvp3LkzISEheY4PHjyY1NRUNmzYkOf4HXfckefrWrVqAbkLfvz7+MWLFy3DBAv6Hl5PixYtsLe3x93dnTvuuIPAwEB++eUXAgIC8rTr16/fda91edW7J5544qptfvvtN7Kzs3n44Yfz1O3k5ET79u1vatW5Pn365Pm6fv36pKenExsbC8Cff/4JwIMPPpin3QMPPJDn6/T0dP744w/uuusuXFxc8tTZq1cv0tPT2bhxo6V9//79eeyxx3jmmWd47bXXeO655+jatesNP49/Mv7ufb08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RKSsUw9WIaVl5VD7xd+s8tj7X+mOi8P13zI3Nzfc3NxYvHgxLVq0wNHR8YrtKlasSJMmTRg5ciQ//fRTofYqurwnWFZW1hXPf/PNN0RERNC3b99850wmE56engAkJyczaNAgPvjgAwDeeecdevXqxZEjR3B3d+f7779n6tSpzJ8/nzp16hAdHc2uXbss1xoyZAgnT55k/vz5BAcHs2jRInr06MGePXuoUaPGFWsLDAxk5cqVPP7441SoUOGqz/Hrr79m7NixbNq0iQ0bNjB48GBat25N165dC/Yi/cOePXvo3r07r776Kl9++SVxcXGMHDmSkSNH5hma+Pbbb/PCCy/w/PPPF+r616rVbDZz99134+fnx8aNG0lKSso3vyw1NZWOHTvStm1b1qxZg52dHa+99ho9evRg9+7d1KxZk//97388/vjjtG7dGnt7e4YNG8abb75JvXr1Cv16iIiIiJRVClhlkJ2dHTNnzmTYsGF88sknNGrUiPbt23PfffdRv359S7thw4ZhGAZVq1alR48e/PTTT3h4eABwxx13EBYWxocffpjv+ikpKUyYMAFbW1vat29/xRqOHDlCRETEdWvt1KlTnq8//fRTvL29Wb16NXfccQeRkZEEBgbSpUsX7O3tqVy5Ms2aNQPg2LFjzJs3jzNnzhAcHAzA008/za+//sqMGTN44403rviY7777Lvfccw+BgYHUqVOHVq1a0bdv33zzqerXr89LL70EQI0aNZg2bRp//PHHDQWst99+mwceeMASbGrUqMEHH3xA+/btmT59uiXcdurUiaeffrrQ179WrStWrODAgQOcPHmSSpUqAfDGG2/keb7z58/HxsaGL774ApPJBMCMGTPw8vJi1apVdOvWjccff5xly5YxcOBAHBwcaNy4MU8++WShaxUREREpyxSwCsnZ3pb9r3S32mMXVL9+/bj99ttZu3YtGzZs4Ndff2XKlCl88cUXDB48mP379zNz5kz27dtHrVq1GDJkCB06dODXX3/F39+fffv2MXDgwDzXbNWqFTY2NqSmphIUFMTMmTOv2nthGIblg/q1xMbG8uKLL7Jy5UpiYmLIyckhNTWVyMhIAO69917ee+89Swjs1asXvXv3xs7Oju3bt2MYBuHh4XmumZGRga+vL5Dbm3fZQw89xCeffELt2rXZu3cv27ZtY926daxZs4be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nHvuuSdr167NunXrsnr16iTJihUrMn78+AwcODBNTU25/fbb097eniTZuHFj5syZk71791Z2wxYvXpwkOXLkSBYsWJBRo0Zl4MCBueqqq7Jx48bqvFAAuh0BC4A+4dprr82ECRPy9NNPJ0lqamqycuXKvP3221mzZk1aWlqyYMGCJMnUqVPz4IMPpqGhITt37szOnTtz9913J0nmzJmTTZs25YknnsiWLVty0003pbm5Oe+9917VXhsA3UepXC6Xq90EABRl9uzZaWtry7PPPnta7ZZbbsmWLVuybdu202pPPfVU5s2blz179iQ5/hmsO+64I21tbZVr3n///YwZMyY7duzIyJEjK+vXX399pkyZkiVLlhT+egDoWfpVuwEAOFvK5XJKpVKSZMOGDVmyZEm2bduWffv2paOjI4cOHcqBAwcycODALh//5ptvplwuZ+zYsaesHz58OMOGDTvj/QPQ/QlYAPQZ77zzTi6++OJ89NFHmTFjRubOnZt777035513Xl5++eXcdtttOXr06O99/LFjx1JbW5s33ngjtbW1p9QGDRp0ptsHoAcQsADoE1paWrJ169bceeedef3119PR0ZHly5enpub4x5GffPLJU67v379/Ojs7T1mbNGlSOjs7s3v37lxzzTVnrXcAeg4BC4Be5/Dhw9m1a1c6Ozvz2WefZf369Vm6dGlmzpyZWbNmZevWreno6MhDDz2UG264IZs2bcqqVatOeY7Ro0envb09L774YiZMmJABAwZk7NixufXWWzNr1qwsX748kyZNyp49e9LS0pLx48dnxowZVXrFAHQXThEEoNdZv359LrjggowePTrNzc3ZsGFDVq5cmbVr16a2tjYTJ07MihUrsmzZsowbNy6PP/54li5despzTJ06NXPnzs3NN9+c888/P/fdd1+S5JFHHsmsWbNy11135dJLL82NN96YV199NU1NTdV4qQB0M04RBAAAKIgdLAAAgIIIWAAAAAURsAAAAAoiYAEAABREwAIAACiIgAUAAFAQAQsAAKAgAhYAAEBBBCwAAICCCFgAAAAFEbAAAAAK8r+4B2iKbd8jNAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualize the S&P Case-Shiller Home Price Index over time\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.plot(df['DATE'], df['CSUSHPISA'], label='S&P Case-Shiller Index')\n",
    "plt.xlabel('Date')\n",
    "plt.ylabel('Home Price Index')\n",
    "plt.title('S&P Case-Shiller Home Price Index Over Time')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6278e8f5",
   "metadata": {},
   "source": [
    "<center>\n",
    "<h1 style=\"font-size: 40px; font-family: serif;\">Train and Testing</h1>\n",
    "</center>\n",
    "<span id=\"Datatcleaning\"></span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d6a776e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Assuming you want to predict future values\n",
    "train_size = int(len(df) * 0.8)\n",
    "train, test = df[:train_size], df[train_size:]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cff857a2",
   "metadata": {},
   "source": [
    "<center>\n",
    "<h1 style=\"font-size: 40px; font-family: serif;\">Model Building</h1>\n",
    "</center>\n",
    "<span id=\"Datatcleaning\"></span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "76e7173d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Linear Regression\n",
    "model = LinearRegression()\n",
    "\n",
    "# Prepare the data\n",
    "X_train, y_train = np.arange(len(train)).reshape(-1, 1), train['CSUSHPISA']\n",
    "X_test, y_test = np.arange(len(train), len(df)).reshape(-1, 1), test['CSUSHPISA']\n",
    "\n",
    "# Train the model\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Predictions\n",
    "train_predictions = model.predict(X_train)\n",
    "test_predictions = model.predict(X_test)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "49198c78",
   "metadata": {},
   "source": [
    "<center>\n",
    "<h1 style=\"font-size: 40px; font-family: serif;\">Model Evaluation</h1>\n",
    "</center>\n",
    "<span id=\"Datatcleaning\"></span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7b376b5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train MSE: 286.9983657134046\n",
      "Test MSE: 2695.148243856247\n"
     ]
    }
   ],
   "source": [
    "# Evaluate the model\n",
    "train_mse = mean_squared_error(y_train, train_predictions)\n",
    "test_mse = mean_squared_error(y_test, test_predictions)\n",
    "\n",
    "print(f'Train MSE: {train_mse}')\n",
    "print(f'Test MSE: {test_mse}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "2983ab67",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-12-16 13:15:34.913 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\ASUS\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Streamlit App\n",
    "st.title('S&P Case-Shiller Home Price Index Prediction App')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5510cdff",
   "metadata": {},
   "source": [
    "<center>\n",
    "<h1 style=\"font-size: 40px; font-family: serif;\">Visualization of Prediction</h1>\n",
    "</center>\n",
    "<span id=\"Datatcleaning\"></span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "64145e3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visualization of Predictions\n",
    "st.subheader('Visualization of Predictions')\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.plot(df['DATE'], df['CSUSHPISA'], label='Actual Index')\n",
    "plt.plot(train['DATE'], train_predictions, label='Train Predictions')\n",
    "plt.plot(test['DATE'], test_predictions, label='Test Predictions')\n",
    "plt.xlabel('Date')\n",
    "plt.ylabel('Home Price Index')\n",
    "plt.title('S&P Case-Shiller Home Price Index Predictions')\n",
    "plt.legend()\n",
    "st.pyplot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "2205c681",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Model Evaluation\n",
    "st.subheader('Model Evaluation')\n",
    "st.write(f'Train Mean Squared Error: {train_mse}')\n",
    "st.write(f'Test Mean Squared Error: {test_mse}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "f241bf62",
   "metadata": {},
   "outputs": [],
   "source": [
    "!streamlit run Homellc.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "7987a2a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
