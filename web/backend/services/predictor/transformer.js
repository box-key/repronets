const axios = require('axios');
const routes = require('../../config').routes;
const logger = require('../../loaders/logger')(module);

module.exports = async function(input, language, beam) {

  params = {
    input: input,
    language: language,
    beam: beam
  };

  return axios.get(routes.transformer, { params: params })
    .then((resp) => {
      logger.debug(`ts outputs = ${JSON.stringify(resp.status)}`);
      return resp.data;
    })
    .catch((err) => {
      logger.error(err);
      return {
      	resp: 500,
      	message: err
      };
    });
};
