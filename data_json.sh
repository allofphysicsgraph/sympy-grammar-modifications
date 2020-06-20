if [[ ! -f data.json ]];
then
 wget https://raw.githubusercontent.com/allofphysicsgraph/proofofconcept/gh-pages/v7_pickle_web_interface/flask/data.json
fi

if [[ ! -f /opt/data.json ]];
then
    cp data.json /opt/data.json
fi