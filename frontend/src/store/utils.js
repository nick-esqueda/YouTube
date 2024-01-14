export const createNormalizedState = (entityArr) => {
    const state = {
        idList: [],
        entities: {},
    };

    return entityArr.reduce((obj, entity) => {
        const dateParts = entity.createdAt.split(' ');
        entity.createdAt = `${dateParts[2]} ${dateParts[1]}, ${dateParts[3]}`
        obj.idList.push(entity.id);
        obj.entities[entity.id] = entity;
        return obj;
    }, state);
}

export const updateNormalizedState = (entityArr, currentState) => {
    const newState = {
        idList: [...currentState.idList],
        entities: {...currentState.entities}
    };
    
    return entityArr.reduce((obj, entity) => {
        const dateParts = entity.createdAt.split(' ');
        entity.createdAt = `${dateParts[2]} ${dateParts[1]}, ${dateParts[3]}`
        obj.idList.push(entity);
        obj.entities[entity.id] = entity;
        return obj;
    }, newState);
}
