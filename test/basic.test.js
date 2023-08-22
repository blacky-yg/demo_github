const assert = require('assert');
const { describe } = require('mocha');

describe('Basic Mocha String Test', () => {
    it('should return number of charachters in a string', () => {
        assert.equal('Hello'.length, 4);
    });
    it('should return first charachter of the string', () => {
        assert.equal('Hello'.charAt(0), 'H');
    });
});
