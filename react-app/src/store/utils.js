export const normalizeOneLevel = (dataArr) => {
    return dataArr.reduce((obj, data) => {
        obj[data.id] = data;
        return obj;
    }, {})
}
