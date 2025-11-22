// types.ts

import { Point } from './geometry';

interface GameEvent {
  timestamp: number;
  type: string;
  payload?: any;
}

interface InputEvent extends GameEvent {
  input: string;
}

interface MovementEvent extends GameEvent {
  type: 'move';
  direction: string;
  position: Point;
}

interface CollisionEvent extends GameEvent {
  type: 'collision';
  entity: string;
}

interface UpdateEvent extends GameEvent {
  type: 'update';
  entity: string;
  properties: { [key: string]: any };
}

interface NewEntityEvent extends GameEvent {
  type: 'newEntity';
  entity: string;
  properties: { [key: string]: any };
}

type Entity = {
  id: string;
  type: string;
  position: Point;
  properties: { [key: string]: any };
};