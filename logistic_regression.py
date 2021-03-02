{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Logistic_Regression.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNW/XuA+aTtt/W7PCOAtKwt",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vdnew/Loan-Prediction/blob/main/logistic_regression.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Na26TjViRPZX"
      },
      "source": [
        "import numpy as np \r\n",
        "import pandas as pd\r\n",
        "import matplotlib.pyplot as plt\r\n",
        "%matplotlib inline\r\n",
        "import seaborn as sns\r\n",
        "sns.set(style=\"white\", color_codes=True)"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yzqolgTlRbVu"
      },
      "source": [
        "path = '/content/train_loanprediction1.csv'\r\n",
        "train = pd.read_csv(path)"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "Yeg8HPIxRmot",
        "outputId": "376ebc4d-c67c-4d18-dd6a-69bc6c849be4"
      },
      "source": [
        "train.head()"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Credit_History Property_Area Loan_Status\n",
              "0  LP001002   Male      No  ...            1.0         Urban           Y\n",
              "1  LP001003   Male     Yes  ...            1.0         Rural           N\n",
              "2  LP001005   Male     Yes  ...            1.0         Urban           Y\n",
              "3  LP001006   Male     Yes  ...            1.0         Urban           Y\n",
              "4  LP001008   Male      No  ...            1.0         Urban           Y\n",
              "\n",
              "[5 rows x 13 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "86WeiKkvR06K",
        "outputId": "9503f505-9757-4c5a-fad4-07f8ae91a061"
      },
      "source": [
        "train.describe()"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>614.000000</td>\n",
              "      <td>614.000000</td>\n",
              "      <td>592.000000</td>\n",
              "      <td>600.00000</td>\n",
              "      <td>564.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>5403.459283</td>\n",
              "      <td>1621.245798</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>342.00000</td>\n",
              "      <td>0.842199</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>6109.041673</td>\n",
              "      <td>2926.248369</td>\n",
              "      <td>85.587325</td>\n",
              "      <td>65.12041</td>\n",
              "      <td>0.364878</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>150.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>9.000000</td>\n",
              "      <td>12.00000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2877.500000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>100.000000</td>\n",
              "      <td>360.00000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>3812.500000</td>\n",
              "      <td>1188.500000</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.00000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>5795.000000</td>\n",
              "      <td>2297.250000</td>\n",
              "      <td>168.000000</td>\n",
              "      <td>360.00000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>81000.000000</td>\n",
              "      <td>41667.000000</td>\n",
              "      <td>700.000000</td>\n",
              "      <td>480.00000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       ApplicantIncome  CoapplicantIncome  ...  Loan_Amount_Term  Credit_History\n",
              "count       614.000000         614.000000  ...         600.00000      564.000000\n",
              "mean       5403.459283        1621.245798  ...         342.00000        0.842199\n",
              "std        6109.041673        2926.248369  ...          65.12041        0.364878\n",
              "min         150.000000           0.000000  ...          12.00000        0.000000\n",
              "25%        2877.500000           0.000000  ...         360.00000        1.000000\n",
              "50%        3812.500000        1188.500000  ...         360.00000        1.000000\n",
              "75%        5795.000000        2297.250000  ...         360.00000        1.000000\n",
              "max       81000.000000       41667.000000  ...         480.00000        1.000000\n",
              "\n",
              "[8 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PVpK8eVjR4gq",
        "outputId": "d7018436-2b34-4d50-e1d7-fff771e069cd"
      },
      "source": [
        "train.info()"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 614 entries, 0 to 613\n",
            "Data columns (total 13 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   Loan_ID            614 non-null    object \n",
            " 1   Gender             601 non-null    object \n",
            " 2   Married            611 non-null    object \n",
            " 3   Dependents         599 non-null    object \n",
            " 4   Education          614 non-null    object \n",
            " 5   Self_Employed      582 non-null    object \n",
            " 6   ApplicantIncome    614 non-null    int64  \n",
            " 7   CoapplicantIncome  614 non-null    float64\n",
            " 8   LoanAmount         592 non-null    float64\n",
            " 9   Loan_Amount_Term   600 non-null    float64\n",
            " 10  Credit_History     564 non-null    float64\n",
            " 11  Property_Area      614 non-null    object \n",
            " 12  Loan_Status        614 non-null    object \n",
            "dtypes: float64(4), int64(1), object(8)\n",
            "memory usage: 62.5+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rTsp2i_hR8fz",
        "outputId": "d3feecae-ea2e-43fa-ab8b-7d34724890da"
      },
      "source": [
        "train.shape"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(614, 13)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aKSjOkN_R_5O",
        "outputId": "fb9a3b9c-9dc1-4b41-d1a5-2cd9df921649"
      },
      "source": [
        "train.isnull().any()"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Loan_ID              False\n",
              "Gender                True\n",
              "Married               True\n",
              "Dependents            True\n",
              "Education            False\n",
              "Self_Employed         True\n",
              "ApplicantIncome      False\n",
              "CoapplicantIncome    False\n",
              "LoanAmount            True\n",
              "Loan_Amount_Term      True\n",
              "Credit_History        True\n",
              "Property_Area        False\n",
              "Loan_Status          False\n",
              "dtype: bool"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gqPDfHTzSCgx",
        "outputId": "1acde3be-5d70-4f90-d3dc-0bf821e01e58"
      },
      "source": [
        "train.isnull().sum()"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Loan_ID               0\n",
              "Gender               13\n",
              "Married               3\n",
              "Dependents           15\n",
              "Education             0\n",
              "Self_Employed        32\n",
              "ApplicantIncome       0\n",
              "CoapplicantIncome     0\n",
              "LoanAmount           22\n",
              "Loan_Amount_Term     14\n",
              "Credit_History       50\n",
              "Property_Area         0\n",
              "Loan_Status           0\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mt1dlpYASG6M",
        "outputId": "d7023009-4eb4-48b8-fc8a-6400fea86e9c"
      },
      "source": [
        "train[['Gender']].info()"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 614 entries, 0 to 613\n",
            "Data columns (total 1 columns):\n",
            " #   Column  Non-Null Count  Dtype \n",
            "---  ------  --------------  ----- \n",
            " 0   Gender  601 non-null    object\n",
            "dtypes: object(1)\n",
            "memory usage: 4.9+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 418
        },
        "id": "3dWwRVQCSLjj",
        "outputId": "7e13066c-7982-4950-f454-10130e2b5b23"
      },
      "source": [
        "train.head(10)"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>LP001011</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>2</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>5417</td>\n",
              "      <td>4196.0</td>\n",
              "      <td>267.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>LP001013</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2333</td>\n",
              "      <td>1516.0</td>\n",
              "      <td>95.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>LP001014</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3+</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>3036</td>\n",
              "      <td>2504.0</td>\n",
              "      <td>158.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Semiurban</td>\n",
              "      <td>N</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>LP001018</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>2</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4006</td>\n",
              "      <td>1526.0</td>\n",
              "      <td>168.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>LP001020</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>12841</td>\n",
              "      <td>10968.0</td>\n",
              "      <td>349.0</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Semiurban</td>\n",
              "      <td>N</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Credit_History Property_Area Loan_Status\n",
              "0  LP001002   Male      No  ...            1.0         Urban           Y\n",
              "1  LP001003   Male     Yes  ...            1.0         Rural           N\n",
              "2  LP001005   Male     Yes  ...            1.0         Urban           Y\n",
              "3  LP001006   Male     Yes  ...            1.0         Urban           Y\n",
              "4  LP001008   Male      No  ...            1.0         Urban           Y\n",
              "5  LP001011   Male     Yes  ...            1.0         Urban           Y\n",
              "6  LP001013   Male     Yes  ...            1.0         Urban           Y\n",
              "7  LP001014   Male     Yes  ...            0.0     Semiurban           N\n",
              "8  LP001018   Male     Yes  ...            1.0         Urban           Y\n",
              "9  LP001020   Male     Yes  ...            1.0     Semiurban           N\n",
              "\n",
              "[10 rows x 13 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9uP9wl0fSO14",
        "outputId": "9ae83045-0632-48ba-f50d-3f12cd6377c7"
      },
      "source": [
        "train['Property_Area'].unique()"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Urban', 'Rural', 'Semiurban'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5Hh0ng8BSUKv",
        "outputId": "9931a638-42f0-4def-c8de-1e3bf2a1fa41"
      },
      "source": [
        "train['Property_Area'].value_counts()"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Semiurban    233\n",
              "Urban        202\n",
              "Rural        179\n",
              "Name: Property_Area, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BbpsOKtZSZUu",
        "outputId": "a0c0451f-76f7-4c25-c623-34213e9010b6"
      },
      "source": [
        "train_loan = train.dropna()\r\n",
        "train_loan.info()"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 480 entries, 1 to 613\n",
            "Data columns (total 13 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   Loan_ID            480 non-null    object \n",
            " 1   Gender             480 non-null    object \n",
            " 2   Married            480 non-null    object \n",
            " 3   Dependents         480 non-null    object \n",
            " 4   Education          480 non-null    object \n",
            " 5   Self_Employed      480 non-null    object \n",
            " 6   ApplicantIncome    480 non-null    int64  \n",
            " 7   CoapplicantIncome  480 non-null    float64\n",
            " 8   LoanAmount         480 non-null    float64\n",
            " 9   Loan_Amount_Term   480 non-null    float64\n",
            " 10  Credit_History     480 non-null    float64\n",
            " 11  Property_Area      480 non-null    object \n",
            " 12  Loan_Status        480 non-null    object \n",
            "dtypes: float64(4), int64(1), object(8)\n",
            "memory usage: 52.5+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w_wFvFLHSgVe",
        "outputId": "d9ce299e-9669-4139-9d63-8cefde4d96b2"
      },
      "source": [
        "train.info()"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 614 entries, 0 to 613\n",
            "Data columns (total 13 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   Loan_ID            614 non-null    object \n",
            " 1   Gender             601 non-null    object \n",
            " 2   Married            611 non-null    object \n",
            " 3   Dependents         599 non-null    object \n",
            " 4   Education          614 non-null    object \n",
            " 5   Self_Employed      582 non-null    object \n",
            " 6   ApplicantIncome    614 non-null    int64  \n",
            " 7   CoapplicantIncome  614 non-null    float64\n",
            " 8   LoanAmount         592 non-null    float64\n",
            " 9   Loan_Amount_Term   600 non-null    float64\n",
            " 10  Credit_History     564 non-null    float64\n",
            " 11  Property_Area      614 non-null    object \n",
            " 12  Loan_Status        614 non-null    object \n",
            "dtypes: float64(4), int64(1), object(8)\n",
            "memory usage: 62.5+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YM92dB2yS43D"
      },
      "source": [
        "<h1> Data Preprocessing </h1>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6EoOOB7OS4Gy",
        "outputId": "78599266-f5fd-4c39-a84b-70b58718297b"
      },
      "source": [
        "train['Dependents'].fillna(1,inplace=True)\r\n",
        "train.info()"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 614 entries, 0 to 613\n",
            "Data columns (total 13 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   Loan_ID            614 non-null    object \n",
            " 1   Gender             601 non-null    object \n",
            " 2   Married            611 non-null    object \n",
            " 3   Dependents         614 non-null    object \n",
            " 4   Education          614 non-null    object \n",
            " 5   Self_Employed      582 non-null    object \n",
            " 6   ApplicantIncome    614 non-null    int64  \n",
            " 7   CoapplicantIncome  614 non-null    float64\n",
            " 8   LoanAmount         592 non-null    float64\n",
            " 9   Loan_Amount_Term   600 non-null    float64\n",
            " 10  Credit_History     564 non-null    float64\n",
            " 11  Property_Area      614 non-null    object \n",
            " 12  Loan_Status        614 non-null    object \n",
            "dtypes: float64(4), int64(1), object(8)\n",
            "memory usage: 62.5+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZMs9ccaWTEBS",
        "outputId": "3f1e072e-78f5-4537-befc-41cc4eaf44d6"
      },
      "source": [
        "train['LoanAmount'].fillna(train.LoanAmount.mean(),inplace=True)\r\n",
        "train.info()"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 614 entries, 0 to 613\n",
            "Data columns (total 13 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   Loan_ID            614 non-null    object \n",
            " 1   Gender             601 non-null    object \n",
            " 2   Married            611 non-null    object \n",
            " 3   Dependents         614 non-null    object \n",
            " 4   Education          614 non-null    object \n",
            " 5   Self_Employed      582 non-null    object \n",
            " 6   ApplicantIncome    614 non-null    int64  \n",
            " 7   CoapplicantIncome  614 non-null    float64\n",
            " 8   LoanAmount         614 non-null    float64\n",
            " 9   Loan_Amount_Term   600 non-null    float64\n",
            " 10  Credit_History     564 non-null    float64\n",
            " 11  Property_Area      614 non-null    object \n",
            " 12  Loan_Status        614 non-null    object \n",
            "dtypes: float64(4), int64(1), object(8)\n",
            "memory usage: 62.5+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 418
        },
        "id": "fbHNAyHlTL_N",
        "outputId": "bf96b4bd-d6f0-4432-bcdc-832cb3f42eba"
      },
      "source": [
        "train.head(10)"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>LP001011</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>2</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>5417</td>\n",
              "      <td>4196.0</td>\n",
              "      <td>267.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>LP001013</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2333</td>\n",
              "      <td>1516.0</td>\n",
              "      <td>95.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>LP001014</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3+</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>3036</td>\n",
              "      <td>2504.0</td>\n",
              "      <td>158.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Semiurban</td>\n",
              "      <td>N</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>LP001018</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>2</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4006</td>\n",
              "      <td>1526.0</td>\n",
              "      <td>168.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>LP001020</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>12841</td>\n",
              "      <td>10968.0</td>\n",
              "      <td>349.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Semiurban</td>\n",
              "      <td>N</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Credit_History Property_Area Loan_Status\n",
              "0  LP001002   Male      No  ...            1.0         Urban           Y\n",
              "1  LP001003   Male     Yes  ...            1.0         Rural           N\n",
              "2  LP001005   Male     Yes  ...            1.0         Urban           Y\n",
              "3  LP001006   Male     Yes  ...            1.0         Urban           Y\n",
              "4  LP001008   Male      No  ...            1.0         Urban           Y\n",
              "5  LP001011   Male     Yes  ...            1.0         Urban           Y\n",
              "6  LP001013   Male     Yes  ...            1.0         Urban           Y\n",
              "7  LP001014   Male     Yes  ...            0.0     Semiurban           N\n",
              "8  LP001018   Male     Yes  ...            1.0         Urban           Y\n",
              "9  LP001020   Male     Yes  ...            1.0     Semiurban           N\n",
              "\n",
              "[10 rows x 13 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "L0Nl-4q3TOWc",
        "outputId": "b865c99b-14b4-485c-db66-947a9448842e"
      },
      "source": [
        "ValueMapping = {'Yes': 1, 'No': 0}\r\n",
        "train['Married_Section'] = train['Married'].map(ValueMapping)\r\n",
        "train.head()"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "      <th>Married_Section</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Property_Area Loan_Status Married_Section\n",
              "0  LP001002   Male      No  ...         Urban           Y             0.0\n",
              "1  LP001003   Male     Yes  ...         Rural           N             1.0\n",
              "2  LP001005   Male     Yes  ...         Urban           Y             1.0\n",
              "3  LP001006   Male     Yes  ...         Urban           Y             1.0\n",
              "4  LP001008   Male      No  ...         Urban           Y             0.0\n",
              "\n",
              "[5 rows x 14 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "yAa9cTtqTdFJ",
        "outputId": "f925288d-8ab5-4c54-dc2f-23bbddd036ab"
      },
      "source": [
        "ValueMapping1 = {'Male': 1, 'Female': 0}\r\n",
        "train['Gender_Section'] = train['Gender'].map(ValueMapping1)\r\n",
        "train.head()"
      ],
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "      <th>Married_Section</th>\n",
              "      <th>Gender_Section</th>\n",
              "      <th>Edu_Section</th>\n",
              "      <th>Employed_Section</th>\n",
              "      <th>Property_Section</th>\n",
              "      <th>Loan_Section</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Employed_Section Property_Section Loan_Section\n",
              "0  LP001002   Male      No  ...              0.0                2            1\n",
              "1  LP001003   Male     Yes  ...              0.0                0            0\n",
              "2  LP001005   Male     Yes  ...              1.0                2            1\n",
              "3  LP001006   Male     Yes  ...              0.0                2            1\n",
              "4  LP001008   Male      No  ...              0.0                2            1\n",
              "\n",
              "[5 rows x 19 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yWMGAfQdTvfW",
        "outputId": "6c073cb3-6ba3-49c5-e3ae-b0d083708db2"
      },
      "source": [
        "train['Education'].unique()"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Graduate', 'Not Graduate'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "qV408vVGT-LG",
        "outputId": "2313c9d6-fe5d-4b40-c9d6-ea77c5418f8e"
      },
      "source": [
        "ValueMapping2 = {'Graduate': 1, 'Not Graduate': 0}\r\n",
        "train['Edu_Section'] = train['Education'].map(ValueMapping2)\r\n",
        "train.head()"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "      <th>Married_Section</th>\n",
              "      <th>Gender_Section</th>\n",
              "      <th>Edu_Section</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Married_Section Gender_Section Edu_Section\n",
              "0  LP001002   Male      No  ...             0.0            1.0           1\n",
              "1  LP001003   Male     Yes  ...             1.0            1.0           1\n",
              "2  LP001005   Male     Yes  ...             1.0            1.0           1\n",
              "3  LP001006   Male     Yes  ...             1.0            1.0           0\n",
              "4  LP001008   Male      No  ...             0.0            1.0           1\n",
              "\n",
              "[5 rows x 16 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m4LRqYADUMqd",
        "outputId": "11428578-ca8d-46ff-ed53-2cb7278501b7"
      },
      "source": [
        "train.info()"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 614 entries, 0 to 613\n",
            "Data columns (total 16 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   Loan_ID            614 non-null    object \n",
            " 1   Gender             601 non-null    object \n",
            " 2   Married            611 non-null    object \n",
            " 3   Dependents         614 non-null    object \n",
            " 4   Education          614 non-null    object \n",
            " 5   Self_Employed      582 non-null    object \n",
            " 6   ApplicantIncome    614 non-null    int64  \n",
            " 7   CoapplicantIncome  614 non-null    float64\n",
            " 8   LoanAmount         614 non-null    float64\n",
            " 9   Loan_Amount_Term   600 non-null    float64\n",
            " 10  Credit_History     564 non-null    float64\n",
            " 11  Property_Area      614 non-null    object \n",
            " 12  Loan_Status        614 non-null    object \n",
            " 13  Married_Section    611 non-null    float64\n",
            " 14  Gender_Section     601 non-null    float64\n",
            " 15  Edu_Section        614 non-null    int64  \n",
            "dtypes: float64(6), int64(2), object(8)\n",
            "memory usage: 76.9+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G8twnWZ2UO2y",
        "outputId": "3dc2efd8-851a-483f-a6cc-f705bb8a898f"
      },
      "source": [
        "train['Married_Section'].fillna(train.Married_Section.mean(), inplace=True)\r\n",
        "train['Gender_Section'].fillna(train.Gender_Section.mean(), inplace=True)\r\n",
        "train['Loan_Amount_Term'].fillna(train.Loan_Amount_Term.mean(), inplace=True)\r\n",
        "train['Credit_History'].fillna(train.Credit_History.mean(), inplace=True)\r\n",
        "\r\n",
        "train.info()"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 614 entries, 0 to 613\n",
            "Data columns (total 16 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   Loan_ID            614 non-null    object \n",
            " 1   Gender             601 non-null    object \n",
            " 2   Married            611 non-null    object \n",
            " 3   Dependents         614 non-null    object \n",
            " 4   Education          614 non-null    object \n",
            " 5   Self_Employed      582 non-null    object \n",
            " 6   ApplicantIncome    614 non-null    int64  \n",
            " 7   CoapplicantIncome  614 non-null    float64\n",
            " 8   LoanAmount         614 non-null    float64\n",
            " 9   Loan_Amount_Term   614 non-null    float64\n",
            " 10  Credit_History     614 non-null    float64\n",
            " 11  Property_Area      614 non-null    object \n",
            " 12  Loan_Status        614 non-null    object \n",
            " 13  Married_Section    614 non-null    float64\n",
            " 14  Gender_Section     614 non-null    float64\n",
            " 15  Edu_Section        614 non-null    int64  \n",
            "dtypes: float64(6), int64(2), object(8)\n",
            "memory usage: 76.9+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "uqcnFnLnUzU5",
        "outputId": "5da78b74-3adb-4725-a2d1-eedd345b3394"
      },
      "source": [
        "ValueMapping3 = {'Yes': 1, 'No': 0}\r\n",
        "train['Employed_Section'] = train['Self_Employed'].map(ValueMapping3)\r\n",
        "\r\n",
        "train.head()"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "      <th>Married_Section</th>\n",
              "      <th>Gender_Section</th>\n",
              "      <th>Edu_Section</th>\n",
              "      <th>Employed_Section</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Gender_Section Edu_Section Employed_Section\n",
              "0  LP001002   Male      No  ...            1.0           1              0.0\n",
              "1  LP001003   Male     Yes  ...            1.0           1              0.0\n",
              "2  LP001005   Male     Yes  ...            1.0           1              1.0\n",
              "3  LP001006   Male     Yes  ...            1.0           0              0.0\n",
              "4  LP001008   Male      No  ...            1.0           1              0.0\n",
              "\n",
              "[5 rows x 17 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AjegjIOyVDI_",
        "outputId": "33d98b9b-63f4-4438-c00d-f80151324f63"
      },
      "source": [
        "train.info()"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 614 entries, 0 to 613\n",
            "Data columns (total 17 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   Loan_ID            614 non-null    object \n",
            " 1   Gender             601 non-null    object \n",
            " 2   Married            611 non-null    object \n",
            " 3   Dependents         614 non-null    object \n",
            " 4   Education          614 non-null    object \n",
            " 5   Self_Employed      582 non-null    object \n",
            " 6   ApplicantIncome    614 non-null    int64  \n",
            " 7   CoapplicantIncome  614 non-null    float64\n",
            " 8   LoanAmount         614 non-null    float64\n",
            " 9   Loan_Amount_Term   614 non-null    float64\n",
            " 10  Credit_History     614 non-null    float64\n",
            " 11  Property_Area      614 non-null    object \n",
            " 12  Loan_Status        614 non-null    object \n",
            " 13  Married_Section    614 non-null    float64\n",
            " 14  Gender_Section     614 non-null    float64\n",
            " 15  Edu_Section        614 non-null    int64  \n",
            " 16  Employed_Section   582 non-null    float64\n",
            "dtypes: float64(7), int64(2), object(8)\n",
            "memory usage: 81.7+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "PGC-hA0QVHSw",
        "outputId": "9850bc17-7d45-40cd-e848-b6442f7d2f98"
      },
      "source": [
        "from sklearn.preprocessing import LabelEncoder\r\n",
        "\r\n",
        "lb = LabelEncoder()\r\n",
        "\r\n",
        "train['Property_Section'] = lb.fit_transform(train['Property_Area'])\r\n",
        "\r\n",
        "train.head()"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "      <th>Married_Section</th>\n",
              "      <th>Gender_Section</th>\n",
              "      <th>Edu_Section</th>\n",
              "      <th>Employed_Section</th>\n",
              "      <th>Property_Section</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Edu_Section Employed_Section Property_Section\n",
              "0  LP001002   Male      No  ...           1              0.0                2\n",
              "1  LP001003   Male     Yes  ...           1              0.0                0\n",
              "2  LP001005   Male     Yes  ...           1              1.0                2\n",
              "3  LP001006   Male     Yes  ...           0              0.0                2\n",
              "4  LP001008   Male      No  ...           1              0.0                2\n",
              "\n",
              "[5 rows x 18 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "F72hYM5NVcZV",
        "outputId": "377923e1-af55-4292-c97d-7ab65a29d5db"
      },
      "source": [
        "ValueMapping4 = {'Y':1, 'N':0}\r\n",
        "train['Loan_Section'] = train['Loan_Status'].map(ValueMapping4)\r\n",
        "\r\n",
        "train.head()"
      ],
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "      <th>Married_Section</th>\n",
              "      <th>Gender_Section</th>\n",
              "      <th>Edu_Section</th>\n",
              "      <th>Employed_Section</th>\n",
              "      <th>Property_Section</th>\n",
              "      <th>Loan_Section</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Employed_Section Property_Section Loan_Section\n",
              "0  LP001002   Male      No  ...              0.0                2            1\n",
              "1  LP001003   Male     Yes  ...              0.0                0            0\n",
              "2  LP001005   Male     Yes  ...              1.0                2            1\n",
              "3  LP001006   Male     Yes  ...              0.0                2            1\n",
              "4  LP001008   Male      No  ...              0.0                2            1\n",
              "\n",
              "[5 rows x 19 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 353
        },
        "id": "utb0IZRbWEYx",
        "outputId": "e61f7d97-d9d0-4529-cbdc-9c595a99dede"
      },
      "source": [
        "sns.FacetGrid(train,hue=\"Gender_Section\",size=4) \\\r\n",
        ".map(plt.scatter,\"Loan_Status\",\"LoanAmount\") \\\r\n",
        ".add_legend()\r\n",
        "plt.show()"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/axisgrid.py:316: UserWarning: The `size` parameter has been renamed to `height`; please update your code.\n",
            "  warnings.warn(msg, UserWarning)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 449.6x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 353
        },
        "id": "GaYwTL3mWGpt",
        "outputId": "853e26ad-2820-4a1d-e3af-0e7a083f9062"
      },
      "source": [
        "sns.FacetGrid(train,hue=\"Property_Section\",size=4) \\\r\n",
        ".map(plt.scatter,\"ApplicantIncome\",\"CoapplicantIncome\") \\\r\n",
        ".add_legend()\r\n",
        "plt.show()"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/axisgrid.py:316: UserWarning: The `size` parameter has been renamed to `height`; please update your code.\n",
            "  warnings.warn(msg, UserWarning)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 397.925x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 482
        },
        "id": "5vUCUVOkWOEd",
        "outputId": "e83aa5c1-65e2-4f8e-8101-f727e42a0a00"
      },
      "source": [
        "plt.figure(figsize = (10,7)) \r\n",
        "x = train[\"LoanAmount\"] \r\n",
        "plt.hist(x, bins = 30, color = \"pink\") \r\n",
        "plt.title(\"Loan taken by Customers\") \r\n",
        "plt.xlabel(\"Loan Figures\") \r\n",
        "plt.ylabel(\"Count\")"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0, 0.5, 'Count')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 30
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x504 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 303
        },
        "id": "oe80Az-4WRay",
        "outputId": "52173865-e1fc-4478-95f8-4fa3a2c100e9"
      },
      "source": [
        "sns.boxplot(x=\"Property_Area\", y=\"Gender_Section\", data=train)"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f70953e0890>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 303
        },
        "id": "yBPax1jTWTsP",
        "outputId": "7c1a35ab-0454-4823-ec90-bd4075bd0d96"
      },
      "source": [
        "sns.boxplot(x=\"Married_Section\", y=\"ApplicantIncome\", data=train)"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f7095453890>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 32
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 286
        },
        "id": "ZpUlR9BGWXXf",
        "outputId": "f9ccb317-a8c1-4a32-dd4c-5c375efbe614"
      },
      "source": [
        "train_temp=train[train[\"Education\"]== \"Graduate\"]\r\n",
        "train_temp[\"Self_Employed\"].hist()"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f7095499250>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 516
        },
        "id": "Z-hwvI70WgO-",
        "outputId": "29c3e572-e605-4e64-8fec-14f2ca737857"
      },
      "source": [
        "sns.FacetGrid(train, hue=\"Credit_History\", size=6).map(sns.kdeplot, \"CoapplicantIncome\").add_legend()"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/axisgrid.py:316: UserWarning: The `size` parameter has been renamed to `height`; please update your code.\n",
            "  warnings.warn(msg, UserWarning)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.FacetGrid at 0x7f7095307bd0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 34
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 593.35x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 535
        },
        "id": "kMG5WOGvWjRu",
        "outputId": "c6d4e90d-a92b-4fc8-b160-e1903ca0b276"
      },
      "source": [
        "cols = ['ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Married_Section',\r\n",
        "        'Gender_Section','Edu_Section','Employed_Section','Property_Section']\r\n",
        "f, ax = plt.subplots(figsize=(10, 7))\r\n",
        "cm = np.corrcoef(train[cols].values.T)\r\n",
        "sns.set(font_scale=1.5)\r\n",
        "hm = sns.heatmap(cm,\r\n",
        "                 cbar=True,\r\n",
        "                 annot=True,\r\n",
        "                 square=True,\r\n",
        "                 fmt='.2f',\r\n",
        "                 annot_kws={'size': 15},\r\n",
        "                 yticklabels=cols,\r\n",
        "                 xticklabels=cols)\r\n",
        "\r\n",
        "plt.show()"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x504 with 2 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ls8lzl-QYSZs",
        "outputId": "142c0918-aa7c-4bbb-9cd0-4d8044151de3"
      },
      "source": [
        "train['Employed_Section'].unique()"
      ],
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 0.,  1., nan])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "dQto5rbEYqGA",
        "outputId": "7bf01d47-f634-4349-cce5-2a60b7758ce9"
      },
      "source": [
        "train['Employed_Section'].fillna(1,inplace=True)\r\n",
        "train.head()"
      ],
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "      <th>Married_Section</th>\n",
              "      <th>Gender_Section</th>\n",
              "      <th>Edu_Section</th>\n",
              "      <th>Employed_Section</th>\n",
              "      <th>Property_Section</th>\n",
              "      <th>Loan_Section</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Employed_Section Property_Section Loan_Section\n",
              "0  LP001002   Male      No  ...              0.0                2            1\n",
              "1  LP001003   Male     Yes  ...              0.0                0            0\n",
              "2  LP001005   Male     Yes  ...              1.0                2            1\n",
              "3  LP001006   Male     Yes  ...              0.0                2            1\n",
              "4  LP001008   Male      No  ...              0.0                2            1\n",
              "\n",
              "[5 rows x 19 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mcFFKInvZIZC",
        "outputId": "53c1890f-cfe4-4bfd-d4a7-b7db535b2f5a"
      },
      "source": [
        "train['Employed_Section'].unique()"
      ],
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0., 1.])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 52
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5YQoRBatZUGH",
        "outputId": "f2abfae1-3013-44b2-e40a-2dfe4bd38ce8"
      },
      "source": [
        "train['Gender_Section'].unique()"
      ],
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 1.,  0., nan])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "BmfiLeA-Zecf",
        "outputId": "4af1cf20-2333-4b64-b21c-c80f4bfdf7fd"
      },
      "source": [
        "train['Gender_Section'].fillna(1,inplace=True)\r\n",
        "train.head()"
      ],
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Loan_ID</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Married</th>\n",
              "      <th>Dependents</th>\n",
              "      <th>Education</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>ApplicantIncome</th>\n",
              "      <th>CoapplicantIncome</th>\n",
              "      <th>LoanAmount</th>\n",
              "      <th>Loan_Amount_Term</th>\n",
              "      <th>Credit_History</th>\n",
              "      <th>Property_Area</th>\n",
              "      <th>Loan_Status</th>\n",
              "      <th>Married_Section</th>\n",
              "      <th>Gender_Section</th>\n",
              "      <th>Edu_Section</th>\n",
              "      <th>Employed_Section</th>\n",
              "      <th>Property_Section</th>\n",
              "      <th>Loan_Section</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>LP001002</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>5849</td>\n",
              "      <td>0.0</td>\n",
              "      <td>146.412162</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>LP001003</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>1</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>4583</td>\n",
              "      <td>1508.0</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Rural</td>\n",
              "      <td>N</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>LP001005</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>66.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>LP001006</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>0</td>\n",
              "      <td>Not Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>2583</td>\n",
              "      <td>2358.0</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>LP001008</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>0</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>No</td>\n",
              "      <td>6000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>141.000000</td>\n",
              "      <td>360.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Y</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Loan_ID Gender Married  ... Employed_Section Property_Section Loan_Section\n",
              "0  LP001002   Male      No  ...              0.0                2            1\n",
              "1  LP001003   Male     Yes  ...              0.0                0            0\n",
              "2  LP001005   Male     Yes  ...              1.0                2            1\n",
              "3  LP001006   Male     Yes  ...              0.0                2            1\n",
              "4  LP001008   Male      No  ...              0.0                2            1\n",
              "\n",
              "[5 rows x 19 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IdQSXHADZi6K",
        "outputId": "e872c52b-6f41-4117-b3d2-8c234ef71bb0"
      },
      "source": [
        "train['Gender_Section'].unique()"
      ],
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1., 0.])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8ldYPQ_hWoGs"
      },
      "source": [
        "from sklearn.linear_model import LogisticRegression\r\n",
        "model = LogisticRegression()"
      ],
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6T6ljSx9WxVC"
      },
      "source": [
        "X=train[['ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Married_Section',\r\n",
        "        'Gender_Section','Edu_Section','Employed_Section','Property_Section']].values\r\n",
        "y=train[[\"Loan_Section\"]].values"
      ],
      "execution_count": 60,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9wCMTHOLWytZ"
      },
      "source": [
        "from sklearn.model_selection import train_test_split\r\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)"
      ],
      "execution_count": 61,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RtQFDcKHW1BQ",
        "outputId": "9278ea8e-f1fc-47fc-9a9e-8faf598bddbf"
      },
      "source": [
        "train.isna().any()"
      ],
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Loan_ID              False\n",
              "Gender                True\n",
              "Married               True\n",
              "Dependents           False\n",
              "Education            False\n",
              "Self_Employed         True\n",
              "ApplicantIncome      False\n",
              "CoapplicantIncome    False\n",
              "LoanAmount           False\n",
              "Loan_Amount_Term     False\n",
              "Credit_History       False\n",
              "Property_Area        False\n",
              "Loan_Status          False\n",
              "Married_Section      False\n",
              "Gender_Section       False\n",
              "Edu_Section          False\n",
              "Employed_Section     False\n",
              "Property_Section     False\n",
              "Loan_Section         False\n",
              "dtype: bool"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 62
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qf3eTvrzW-NL",
        "outputId": "91437b15-dd0c-4a22-cfa2-e1938cb75f8c"
      },
      "source": [
        "model.fit(X_train, y_train)"
      ],
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/validation.py:760: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
            "  y = column_or_1d(y, warn=True)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
              "                   intercept_scaling=1, l1_ratio=None, max_iter=100,\n",
              "                   multi_class='auto', n_jobs=None, penalty='l2',\n",
              "                   random_state=None, solver='lbfgs', tol=0.0001, verbose=0,\n",
              "                   warm_start=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 63
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x50lxjYcZRfh",
        "outputId": "9dd0d9ff-e0c0-4dcc-f34f-55ceebfe3640"
      },
      "source": [
        "model.score(X_train,y_train)"
      ],
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.8018648018648019"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 64
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l1N-lyqVZuTo",
        "outputId": "15a65784-0d79-431c-da60-1cfb989df41b"
      },
      "source": [
        "model.score(X_test,y_test)"
      ],
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.8324324324324325"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 65
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yfDBC11aZybT"
      },
      "source": [
        "expected = y_test\r\n",
        "predicted = model.predict(X_test)"
      ],
      "execution_count": 66,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4tGyJFouZ02c",
        "outputId": "14d1dad1-35b3-4d1a-e5d7-0f63312ce0d8"
      },
      "source": [
        "from sklearn import metrics\r\n",
        "print(metrics.classification_report(expected, predicted))"
      ],
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.88      0.45      0.60        51\n",
            "           1       0.82      0.98      0.89       134\n",
            "\n",
            "    accuracy                           0.83       185\n",
            "   macro avg       0.85      0.71      0.75       185\n",
            "weighted avg       0.84      0.83      0.81       185\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T9x3hpEmZ3kI",
        "outputId": "14a320dd-6240-4976-d5f2-601c678bd620"
      },
      "source": [
        "metrics.confusion_matrix(expected, predicted)"
      ],
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 23,  28],\n",
              "       [  3, 131]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 71
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Fg3ARO_RZ5ib"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}