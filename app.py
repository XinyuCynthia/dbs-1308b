{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1d763d47",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,render_template,request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f23702f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "09cf07ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7133d210",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        print(rates)\n",
    "        model1 = joblib.load(\"regression_DBS\")\n",
    "        pred1 = model1.predict([[rates]])\n",
    "        model2 = joblib.load(\"tree_DBS\")\n",
    "        pred2 = model2.predict([[rates]])        \n",
    "        return(render_template(\"index.html\",result1=pred1,result2=pred2))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result1=\"waiting\",result2=\"waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f28f7c96",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [13/Aug/2022 16:16:35] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [13/Aug/2022 16:16:40] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [13/Aug/2022 16:18:25] \"GET / HTTP/1.1\" 200 -\n",
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [13/Aug/2022 16:18:29] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [13/Aug/2022 16:51:58] \"GET / HTTP/1.1\" 200 -\n",
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [13/Aug/2022 16:52:01] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    }
   ],
   "source": [
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1f0e10c",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
